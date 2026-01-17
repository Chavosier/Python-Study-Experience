'''
说明
输入一个正整数n，分解为质因数乘积
如12=2*2*3
输入格式
一行一个正整数
'输出格式
一行乘积表达式
输入数据 1
12
输出数据 1
2*2*3
提示
本题中n小于等于10^9，同时我们认为1有且只有一个质因数是1
'''
n = int(input())
if n == 1:
    print(1)
else:
    f=[]
    d = 2
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    if n > 1:
        f.append(n)
    for ff in f[:-1]:
        print(ff,end='*')
    print(f[-1])