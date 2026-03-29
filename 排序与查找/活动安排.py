'''
题目描述
给定 n 个活动，每个活动 i 有一个起始时间 s_i 和结束时间 f_i （s_i < f_i）。同一时间只能有一个活动进行。如果两个活动的时间区间 [s_i, f_i) 和 [s_j, f_j) 不重叠，则它们是兼容的。请你选出最大数目的互不重叠的活动。

输入格式
第一行：一个整数 n
接下来的 n 行：每行两个整数 s_i 和 f_i
输出格式
输出一个整数，表示最大可选活动数
'''
n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
i=0
while i<n-1:
    for j in range(0,n-i-1):
        if data[j][1]>data[j+1][1]:
            data[j],data[j+1]=data[j+1],data[j]
    i+=1
last=data[0][1]
s=1
i=1
while i<n:
    if data[i][0]>=last:
        s+=1
        last=data[i][1]
    else:
        i+=1
print(s)