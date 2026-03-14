'''
Description
给出一个非升序序列，以及整数a和b。

请你从小到大依次输出该序列中所有在区间[a,b]中的元素以及元素的总个数。

若区间中不存在任何元素，则直接输出-1。

Format
Input
第一行，若干个数据，组成一个非升序序列（存在相同元素） 第二行，给定两个整数：a,b（a<=b）

Output
从小到大依次输出该序列中所有在区间[a,b]中的元素以及元素的总个数。若区间中不存在任何元素，则直接输出-1。

Samples
输入数据 1
25 24 24 24 22 18 14 12 12 11
10 20
输出数据 1
11 12 12 14 18
5
'''
l_helper=list(map(int,input().split()))
a,b=map(int,input().split())

def Print(l):
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[-1])

l=[]
for i in range(len(l_helper)):
    if a<=l_helper[i]<=b:
        l.append(l_helper[i])
if len(l)==0:
    print(-1)
else:
    n=len(l)
    i=0
    while i<n-1:
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        i+=1
    Print(l)
    print(n)

