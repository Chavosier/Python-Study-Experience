# 说明
# 大部分元素是0的矩阵称为稀疏矩阵，假设有k个非零元素，
# 则可把稀疏矩阵用k×3的矩阵简记，其中第一列是行号，第二列是列号，第三列是该行、该列下的非零元素的值。

# 输入格式
# 第一行两个整数m, n，表示原矩阵有m行n列 (m, n⩽1000)
# 以下m行表示原矩阵中元素

# 输出格式
# 第一行一个整数，代表非零元素个数
# 接下来若干行，每行3个元素，分别为行号、列号、元素。

m,n=map(int,input().split())
a=[]
for i in range(m):
    s=list(map(int,input().split()))
    for j in range(n):
        if s[j]!=0:
            a.append([i+1,j+1,s[j]])
print(len(a))
for k in a:
    for w in k:
        print(w,end=' ')
    print()