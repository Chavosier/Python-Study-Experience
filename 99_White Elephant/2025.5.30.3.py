def myjz(x):  # 获取位置值 x 的位置密钥值
    row = (x - 1) // n
    col = (x - 1) % n
    if row % 2 == 1:
        col = n - 1 - col  # 填补①
    return a[row][col]

import random

p = input("请输入明文：")
b = [[0 for j in range(2)] for i in range(len(p))]  # b 数组存储原文的编码值及位置值
for i in range(len(p)):
    for j in range(2):
        if j == 0:
            b[i][j] = ord(p[i])-ord('A') + 1  # 填补②
        else:
            b[i][j] = i + 1

n = int(input("请输入密钥矩阵规模 n："))
flag = [False] * (n * n + 1)
a = [[0 for i in range(n)] for j in range(n)]
i = 0
while i < n:  # 生成 1~n*n 范围内的不重复密钥矩阵，存入二维数组 a 中
    j = 0
    while j < n:
        a[i][j] = random.randint(1, n * n)
        if flag[a[i][j]] == False:
            flag[a[i][j]] = True  # 填补③
            j += 1
    i += 1

print("生成的密钥矩阵为：")
for i in range(n):
    print(a[i])

mw = []
for i in range(len(p)):  # 生成密文 mw
    jmz = b[i][0] + myjz(i+1)  # 填补④
    mw.append(jmz)
    mw.append(i + 1)

print("生成的密文为：")
print(mw)