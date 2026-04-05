'''
说明
给出有n个元素的由小到大的序列，请你编程找出某元素第一次出现的位置。(n<=10^6)
输入格式
第一行：一个整数，表示由小到大序列元素个数；下面n行，每行一个整数；最后一行一个整数x，表示待查找的元素；
'输出格式
如果x在序列中，则输出x第一次出现的位置，否则输出-1。
输入数据 1
5
3
5
6
6
7
6
输出数据 1
3
'''
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
target=int(input())
L=0;R=n-1
t='Chavosier'
while L!=R:
    mid=(L+R)//2
    if l[mid]<target:
        L=mid+1
    elif l[mid]>target:
        R=mid-1
    else:
        t=mid
        break
if l[L]==target:
    t=L
if t=='Chavosier':
    print('-1')
else:
    for i in range(t,-1,-1):
        if l[i]!=target:
            print(i+2)
            break
