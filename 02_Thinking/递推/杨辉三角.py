'''
说明
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
……
输入格式
一行n（3<=n<=30）
输出格式
n 行的杨辉三角形，用空格隔开，行尾无空格。
输入数据 1

3
输出数据 1

1
1 1
1 2 1
提示：推荐使用滚动数组，算法空间复杂度优化
'''
n = int(input())
t   = [[1]]
for i in range(1, n):
    r = [1]
    for j in range(1, i):
        r.append(t[i-1][j-1] + t[i-1][j])
    r.append(1)
    t.append(r)
for r in t:
    print(' '.join(map(str, r)))