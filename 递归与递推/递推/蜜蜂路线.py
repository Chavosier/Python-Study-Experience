'''
说明
一只蜜蜂在下图所示的数字蜂房上爬动,已知它只能从标号小的蜂房爬到标号大的相邻蜂房,现在问你：蜜蜂从蜂房M开始爬到蜂房N，M<N，有多少种爬行路线？
img

输入格式
输入M，N的值。
输出格式
爬行有多少种路线。
输入数据 1
1 14
输出数据 1
377
'''
m,n=map(int,input().split())
def f(a,b):
    if a+1==b:
        return 1
    if a+2==b:
        return 2
    return f(a+1,b)+f(a+2,b)
l=f(m,n)
print(l)