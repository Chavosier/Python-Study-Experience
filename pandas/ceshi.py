def encrypt_4digit(s):
    # 将4位字符串转换为整数
    x = int(s)
    # 使用线性同余加密：y = (k * x) mod 1000000
    k = 123457  # 与1000000互质的常数
    y = (k * x) % 1000000
    # 格式化为6位字符串，不足位补0
    return str(y).zfill(6)

def decrypt_6digit(s):
    # 将6位字符串转换为整数
    y = int(s)
    # 计算逆元常数（k的模1000000逆元）
    inv = 470593
    # 计算候选值：x0 = (inv * y) mod 1000000
    x0 = (inv * y) % 1000000
    # 如果x0在0-9999范围内，直接使用；否则取后4位
    res = x0 if x0 < 10000 else x0 % 10000
    # 格式化为4位字符串，不足位补0
    return str(res).zfill(4)
n=input("请输入4位数字:")
print("加密后:",encrypt_4digit(n))
print("解密后:",decrypt_6digit(encrypt_4digit(n)))