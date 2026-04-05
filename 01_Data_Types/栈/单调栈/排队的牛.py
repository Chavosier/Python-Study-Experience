"""
Description:
农夫约翰有 N 头奶牛正在过乱头发节。

每一头牛都站在同一排面朝右，它们被从左到右依次编号为 1, 2, ⋯, N。编号为 i 的牛身高为 h_i。
第 N 头牛在最前面，而第 1 头牛在最后面。

对于第 i 头牛前面的第 j 头牛，如果 h_i > h_{i+1}, h_i > h_{i+2}, ⋯, h_i > h_j，
那么认为第 i 头牛可以看到第 i+1 到第 j 头牛。

定义 C_i 为第 i 头牛所能看到的牛的数量。请帮助农夫约翰求出 C_1 + C_2 + ⋯ + C_N。

Input:
输入共 N+1 行。
第一行为一个整数 N，代表牛的个数。
接下来 N 行，每行一个整数 a_i，分别代表第 1, 2, ⋯, N 头牛的身高。

Output:
输出共一行一个整数，代表 C_1 + C_2 + ⋯ + C_N。

Samples:
输入数据 1:
6
10
3
7
4
12
2
输出数据 1:
5
"""
n=int(input());sum=0
l=[int(input()) for i in range(n)]
flush=[max(l)+1]
for i in range(n):
    k=0;cur=l[i]
    while flush[k]>cur:
        k+=1
    flush=[cur]+flush[k:]
    sum+=len(flush)-2
print(sum)