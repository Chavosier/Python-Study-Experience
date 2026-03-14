'''
说明
现有n个正整数，n≤10000，要求出这n个正整数中的第k个最小整数（相同大小的整数只计算一次），k≤1000，正整数均小于30000。
输入格式
第一行为n和k，第二行开始为n个正整数的值，整数间用空格隔开。
'输出格式
第k个最小整数的值；若无解，则输出“NO RESULT”。
输入数据 1
10 3
1 3 3 7 2 5 1 2 4 6
输出数据 1
3
'''
ha=[0]*10001
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    ha[l[i]]+=1
s=0
flag=False
for i in range(10001):
    if ha[i]>0:
        s+=1
    if s==k:
        flag=True
        break
if flag:
    print(i)
else:
    print('NO RESULT')
'''
10 999
1 3 3 7 2 5 1 2 4 6
'''