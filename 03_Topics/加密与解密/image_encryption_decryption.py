# ============================================
# 通用导入（所有方法共用）
# ============================================
from PIL import Image  # 从Pillow库中导入Image模块,用于打开\处理和保存图像
import numpy as np  # Numpy库用于数组运算(图像在计算机中本质上就是三维数组)
import matplotlib.pyplot as plt  # 导入Matplotlib的pyplot模块用于并排显示图像


# ============================================
# 方法一、移位加密、解密
# ============================================

# ---------- 参考代码1（逐像素循环处理） ----------
SHIFT = 97  # 加密时每个像素加上这个值(模256)，解密加上(256-SHIFT)=206

def encrypt(img_array):
    tmp = [[0] * WIDTH for i in range(HEIGH)]
    for i in range(HEIGH):
        for j in range(WIDTH):
            r, g, b = img_array[i][j]
            r1 = (r + SHIFT) % 256  # 01. %256后数据会自动转换成int
            g1 = (g + SHIFT) % 256
            b1 = (b + SHIFT) % 256
            tmp[i][j] = (g1, b1, r1)
    # 02. 将tmp列表中的int类型转换回uint8类型后存储返回(jpg图像类型)
    return np.array(tmp, dtype=np.uint8)

def decrypt(enc_array):
    tmp = [[0] * WIDTH for i in range(HEIGH)]
    for i in range(HEIGH):
        for j in range(WIDTH):
            r, g, b = enc_array[i][j]
            r1 = (r - SHIFT + 256) % 256
            g1 = (g - SHIFT + 256) % 256
            b1 = (b - SHIFT + 256) % 256
            tmp[i][j] = (b1, r1, g1)
    return np.array(tmp, dtype=np.uint8)


# ---------- 参考代码2（直接对图像通道处理 - 向量化） ----------
SHIFT = 197  # 加密时每个像素加上这个值(模256)，解密加上(256-SHIFT)=206

def encrypt(img_array):  # 原始图像的Numpy数组（形状为高度，宽度，3），数据类型为uint8
    # img_array[:,:,0]表示所有行，所有列的第0个通道(红色分量),得到一个二维数组r
    r, g, b = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    return np.stack([(b + SHIFT) % 256, (g + SHIFT) % 256, (r + SHIFT) % 256], axis=2)

def decrypt(enc_array):
    b, g, r = enc_array[:,:,0], enc_array[:,:,1], enc_array[:,:,2]
    return np.stack([(r + 256 - SHIFT) % 256, (g + 256 - SHIFT) % 256, (b + 256 - SHIFT) % 256], axis=2)


# ============================================
# 方法二、异或运算加密、解密
# ============================================

# ---------- 参考代码1（逐像素异或） ----------
SHIFT = 170  # 定义常量SHIFT,值为170.加密时每个像素分量偶数位置取反

def encrypt(img_array):  # 原始图像的Numpy数组（形状为高度，宽度，3），数据类型为uint8
    tmp = [[0] * WIDTH for i in range(HEIGH)]
    for i in range(HEIGH):
        for j in range(WIDTH):
            r, g, b = img_array[i][j]
            tmp[i][j] = (r ^ SHIFT, g ^ SHIFT, b ^ SHIFT)
    return tmp

def decrypt(enc_array):
    tmp = [[0] * WIDTH for i in range(HEIGH)]
    for i in range(HEIGH):
        for j in range(WIDTH):
            r, g, b = enc_array[i][j]
            tmp[i][j] = (r ^ SHIFT, g ^ SHIFT, b ^ SHIFT)
    return tmp


# ============================================
# 方法三、选择密钥图像异或加密、解密
# ============================================

# ---------- 参考代码1（逐像素循环，使用全局mask） ----------
def encrypt(img_array):  # 原始图像的Numpy数组（形状为高度，宽度，3），数据类型为uint8
    tmp = [[0] * width1 for i in range(height1)]  # 不要写反次序
    for i in range(height1):
        for j in range(width1):
            r1, g1, b1 = img_array[i][j]
            r2, g2, b2 = mask[i % height2][j % width2]  #
            tmp[i][j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)
    return tmp

def decrypt(enc_array):
    tmp = [[0] * width1 for i in range(height1)]
    for i in range(height1):
        for j in range(width1):
            r1, g1, b1 = enc_array[i][j]
            r2, g2, b2 = mask[i % height2][j % width2]
            tmp[i][j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)
    return tmp


# ---------- 参考代码2（函数参数传递mask，更规范） ----------
def encrypt(img_array, mask):
    h, w, _ = img_array.shape
    mh, mw, _ = mask.shape
    result = np.empty_like(img_array)
    for i in range(h):
        for j in range(w):
            r1, g1, b1 = img_array[i, j]
            r2, g2, b2 = mask[i % mh, j % mw]  # 循环使用掩码像素
            result[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)
    return result

def decrypt(enc_array, mask):
    # 异或加密解密相同
    return encrypt(enc_array, mask)


# ============================================
# 主程序示例（方法一参考代码1的完整流程）
# ============================================
if __name__ == "__main__":
    # 1.读取图像
    img = Image.open("p001.jpg")
    # 2.图像的大小
    WIDTH, HEIGH = img.size
    # 3.numpy将图像处理成数组数据
    original = np.array(img)

    # 加密与解密
    encrypted = encrypt(original)  # 4.加密图像
    decrypted = decrypt(encrypted)  # 5.解密图像

    # 6.将数组数据转换成图像
    img2 = Image.fromarray(encrypted)
    # img2.show()  # 7-1.图像呈现
    img2.save("encrypted.png")  # 7-2.将加密后的图像另保存PNG格式(不丢失信息)

    # 7-3.利用绘图模块并排显示
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    titles = ["Original", "Encrypted", "Decrypted"]
    for ax, data, title in zip(axes, [original, encrypted, decrypted], titles):
        ax.imshow(data)
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


# ============================================
# 主程序示例（方法一参考代码2的完整流程）
# ============================================
if __name__ == "__main__":
    # 读取图像
    img = Image.open("004.jpg")
    original = np.array(img)

    # 加密与解密
    encrypted = encrypt(original)
    decrypted = decrypt(encrypted)

    # 并排显示
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    titles = ["Original", "Encrypted", "Decrypted"]
    for ax, data, title in zip(axes, [original, encrypted, decrypted], titles):
        ax.imshow(data)
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


# ============================================
# 主程序示例（方法二参考代码1的完整流程）
# ============================================
if __name__ == "__main__":
    # 读取图像
    img = Image.open("004.jpg")
    WIDTH, HEIGH = img.size
    original = np.array(img)

    # 加密与解密
    encrypted = encrypt(original)
    decrypted = decrypt(encrypted)

    # 并排显示
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    titles = ["Original", "Encrypted", "Decrypted"]
    for ax, data, title in zip(axes, [original, encrypted, decrypted], titles):
        ax.imshow(data)
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


# ============================================
# 主程序示例（方法三参考代码1的完整流程）
# ============================================
if __name__ == "__main__":
    # 读取图像
    img1 = Image.open("004.jpg")
    img2 = Image.open("mask2.jpg")
    width1, height1 = img1.size
    width2, height2 = img2.size
    original = np.array(img1)
    mask = np.array(img2)

    # 加密与解密
    encrypted = encrypt(original)
    decrypted = decrypt(encrypted)

    # 并排显示
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    titles = ["Original", "Encrypted", "Decrypted"]
    for ax, data, title in zip(axes, [original, encrypted, decrypted], titles):
        ax.imshow(data)
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


# ============================================
# 主程序示例（方法三参考代码2的完整流程）
# ============================================
if __name__ == "__main__":
    # 读取原始图像和掩码图像
    img1 = Image.open("004.jpg")
    img2 = Image.open("mask2.jpg")
    original = np.array(img1)
    mask = np.array(img2)

    encrypted = encrypt(original, mask)
    decrypted = decrypt(encrypted, mask)

    # 并排显示
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    titles = ["Original", "Encrypted", "Decrypted"]
    for ax, data, title in zip(axes, [original, encrypted, decrypted], titles):
        ax.imshow(data)
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


# ============================================
# 思考：探究新的加密、解密方式
# ============================================
