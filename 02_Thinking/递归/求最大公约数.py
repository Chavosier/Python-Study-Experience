'''
说明
用递归方法求两个数 m 和 n 的最大公约数。(m>0，n>0)
输入格式
输入二个数，即m 和 n 的值。
'输出格式
输出最大公约数。
输入数据 1
8 6
输出数据 1
gcd=2
'''
m=list(map(int,input().split()))
def f(a):
    if a[0]==a[1]:
        print('gcd='+str(a[0]))
        exit()
    else:
        a[0], a[1] = max(a), min(a)
        a[0]=a[0]-a[1]
        a[0], a[1] = max(a), min(a)
        f(a)
f(m)