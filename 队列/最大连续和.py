'''
题目描述
给你一个长度为 n 的整数序列 {A1, A2, ⋯, An}，要求从中找出一段连续的长度不超过 m 的非空子序列，
使得这个序列的和最大。

输入格式
第一行为两个整数 n, m；
第二行为 n 个用空格分开的整数序列，每个数的绝对值都小于 1000。

输出格式
仅一个整数，表示连续长度不超过 m 的最大非空子序列和。

样例
输入数据 1
6 4
1 -3 5 1 -2 3

输出数据 1
7
'''
n,m=map(int,input().split());l=list(map(int,input().split()));ans=-10**9
for i in range(n):
    l_sum=[];sum=0
    for j in range(i,min(n,i+m)): sum+=l[j];l_sum.append(sum);might=max(l_sum)
    ans=max(ans,might)    
print(ans)


