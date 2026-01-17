'''
Description
img

Format
Input
输入两个正整数n和k（n>=k, 且n<=50）

Output
输出组合数 C_n^k的值

Samples
输入数据 1
4 2 
输出数据 1
6
'''
n,k=map(int,input().split())
if k>n-k:# c(n,k)=c(n,n-k)
    k=n-k
r=[1]+[0]*k
for i in range(1,n+1):
    for j in range(min(i,k),0,-1):
        # 有下一行可知，相加只用到上一行的数据，
        # 因此可以用一维数组从后向前更新，而且不需要位置大于k的值
        r[j]+=r[j-1]
print(r[k])