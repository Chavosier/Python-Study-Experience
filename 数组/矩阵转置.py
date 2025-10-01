# Description
# 输入一个 n 行 m 列的矩阵 A，将它进行转置后输出。

# Format
# Input
# 第一行包含两个整数 n (1⩽n⩽100) 和 m (1⩽m⩽100)，表示矩阵 A 的行数和列数。
# 接下来 n 行，每行 m 个整数，表示矩阵 A 的元素。相邻两个整数之间用单个空格隔开，每个元素均在 1~1000 之间。

# Output
# 输出 m 行，每行 n 个整数，为矩阵 A 的转置。相邻两个整数之间用单个空格隔开。
n,m=map(int,input().split())
a=[]
for _ in range(n):
    s=list(map(int,input().split()))
    a.append(s)
# print(a)
b=[]
for j in range(m):
    s=[]
    for i in range(n):
        s.append(a[i][j])
    b.append(s)
# print(b)
for k in b:
    for w in k:
        print(w,end=' ')
    print()