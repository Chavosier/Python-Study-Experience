'''
说明
用递归算法，求N！的精确值(N以一般整数输入，且N小于等100)。

输入格式
一行，一个数

输出格式
N!的结果

输入数据 1
10
输出数据 1
3628800
'''
n=int(input())
def f(x):
    if x==1:
        return 1
    ans=x*f(x-1)
    return ans
print(f(n))