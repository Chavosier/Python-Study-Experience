import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib

# 设置中文字体（如有需要）
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ============ 参数设置 ============
n = 50              # 螺旋层数（控制大小）
point_size = 0.6    # 点的大小
figsize = 10        # 图像尺寸（英寸）
dpi = 300           # 分辨率

# ============ 质数判断函数 ============
def is_prime(num):
    """判断是否为质数"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# ============ 生成乌拉姆螺旋坐标 ============
def generate_spiral(n_layers):
    """
    生成乌拉姆螺旋坐标
    从中心开始，方向：右→上→左→下，循环
    返回: (x_coords, y_coords) 的列表
    """
    total = (2 * n_layers + 1) ** 2
    x, y = 0, 0
    coords = [(x, y)]
    
    # 方向: 右, 上, 左, 下
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_idx = 0
    
    step = 1
    count = 1
    
    while count < total:
        # 每个方向走 step 步
        dx, dy = directions[dir_idx]
        for _ in range(step):
            x += dx
            y += dy
            coords.append((x, y))
            count += 1
            if count >= total:
                break
        
        # 转向
        dir_idx = (dir_idx + 1) % 4
        
        # 每转两次方向，步长加1
        if dir_idx % 2 == 0:
            step += 1
    
    return coords

# ============ 生成数据 ============
print("正在生成螺旋坐标...")
coords = generate_spiral(n)
total_numbers = len(coords)
numbers = list(range(1, total_numbers + 1))

print(f"总数字数量: {total_numbers}")

# 判断质数
print("正在判断质数...")
prime_flags = [is_prime(i) for i in numbers]

# 分离坐标
prime_coords = [coords[i] for i in range(total_numbers) if prime_flags[i]]
composite_coords = [coords[i] for i in range(total_numbers) if not prime_flags[i]]

print(f"质数数量: {len(prime_coords)}")
print(f"质数密度: {len(prime_coords)/total_numbers*100:.2f}%")

# ============ 绘制图像 ============
print("正在绘制...")

fig, ax = plt.subplots(figsize=(figsize, figsize))

# 提取坐标
if composite_coords:
    comp_x, comp_y = zip(*composite_coords)
    ax.scatter(comp_x, comp_y, s=point_size*20, c='lightgray', 
               marker='o', edgecolors='none', zorder=1)

if prime_coords:
    prime_x, prime_y = zip(*prime_coords)
    ax.scatter(prime_x, prime_y, s=point_size*20, c='black', 
               marker='o', edgecolors='none', zorder=2)

# 设置坐标轴
ax.set_aspect('equal')
ax.set_xlim(-n-2, n+2)
ax.set_ylim(-n-2, n+2)

# 移除坐标轴
ax.axis('off')

# 设置背景色为白色
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 添加标题
ax.set_title(f'Ulam Spiral (n={n}, {len(prime_coords)} primes)', 
             fontsize=14, pad=10)

plt.tight_layout()

# 保存图像
filename = f'UlamSpiral_n{n}.png'
plt.savefig(filename, dpi=dpi, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print(f"图像已保存: {filename}")

# 显示图像
plt.show()

print("完成!")
