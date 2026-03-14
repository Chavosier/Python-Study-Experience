'''
说明
在一个旧式的火车站旁边有一座桥，其桥面可以绕河中心的桥墩水平旋转。一个车站的职工发现桥的长度最多能容纳两节车厢，如果将桥旋转180度，则可以把相邻两节车厢的位置交换，用这种方法可以重新排列车厢的顺序。于是他就负责用这座桥将进站的车厢按车厢号从小到大排列。他退休后，火车站决定将这一工作自动化，其中一项重要的工作是编一个程序，输入初始的车厢顺序，计算最少用多少步就能将车厢排序。

输入格式
输入文件可能有多行数据，第一行是车厢总数N（不大于10000），后面若干行，共有N个不同的数表示初始的车厢顺序（N个数据可能在一行，也可能出现在多行）。

输出格式
一个数据，是最少的旋转次数。

样例
输入数据 1
4
4 3 2 1
输出数据 1
6
'''
# n=int(input())
# data=[]
# for i in range(n):
#     data.append(list(map(int,input().split())))
# i=0
# while i<n-1:
#     for j in range(0,n-i-1):
#         if data[j][0]>data[j+1][0] or (data[j][0]==data[j+1][0] and data[j][1]>data[j+1][1]):
#             data[j],data[j+1]=data[j+1],data[j]
#     i+=1
# print(data)
import sys
n=int(input())
l=[]
for line in sys.stdin:
    t=list(map(int,line.split()))
    l=l+t
def Print(l):
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[-1])


q,w,e=0,0,0
i=0
while i< n-1:

    for j in range(n-1,(n-1)-(n-i-1),-1):
        w+=1
        if l[j]<l[j-1]:
            e+=1
            l[j],l[j-1]=l[j-1],l[j]
    i+=1


print(str(e))