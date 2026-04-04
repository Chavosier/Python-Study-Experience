'''
Description
给出若干个整数序列，以及整数a和b。

请你从小到大依次输出该序列中所有在区间[a,b]中的元素以及元素的总个数。

若区间中不存在任何元素，则直接输出-1。

Format
Input
第一行，输入若干个整数（存在相同元素）

第二行，给定两个整数：a,b（a<=b）

Output
从小到大依次输出该序列中所有在区间[a,b]中的元素以及元素的总个数。若区间中不存在任何元素，则直接输出-1。

Samples
输入数据 1
25 24 14 12 12 11 24 24 22 18 
10 20
输出数据 1
11 12 12 14 18
5
'''
l_helper=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(len(l_helper)):
    if a<=l_helper[i]<=b:
        l.append(l_helper[i])
n=len(l)

i=0
while i<n-1:
    k=i;i=n
    for j in range(n-1,k,-1):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
            i=j
if n==0:
    print(-1)
    exit()
for i in range(n-1):
    print(l[i],end=' ')
print(l[n-1])
print(n)