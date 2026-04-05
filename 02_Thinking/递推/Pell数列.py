'''
Description
某Pell数列 a1, a2, a3, ..., an 的定义如下：
a1 = 1
a2 = 2
a3 = 3
an = an-3 + 2*an-2 + an-1 (3 < n <= 35)

Format
Input
请输入一个正整数n

Output
第一行输出Pell数列中 an 项的值。
若采用递归方式处理，请计算递归调用总次数，并在第二行输出。

Samples
输入数据 1
4
输出数据 1
8
4
'''
n=int(input())
t=0
'''
n=8
1 2 3 4 5 6 7 8
              1
        1 1 1 
  1 2 3
3 3 3                
'''
def runnum(x):
    if 1<=x<=3:
        return 1
    else:
        s=0
        a=1;b=0;c=0
        for i in range(n,3,-1):
            s+=a
            a,b,c=a+b+c,a,b
        s+=a+b+c+b
        return s
if 1<=n<=3:
    print(n)
    print(1)
else:
    q=1
    w=2
    e=3
    for i in range(n-3):
        q,w,e=w,e,q+2*w+e
    print(e)# 输出Pell数列中 an 项的值
    print(runnum(n))