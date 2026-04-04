'''
Description
给出若干个区间，每个区间可由一个左端点和右端点组成，要求实现区间的合并。
输入格式
 
第 1 行为区间个数 n（n < 5000）
 
第 2 行开始直至第 n+1 行，每行两个整数，表示每个区间的左端点和右端点
输出格式
 
第 1 行为合并后的区间个数 m
 
第 2 行开始直至第 m+1 行，每行两个整数，表示合并后每个区间的左端点和右

Samples
输入数据 1
6
15 18
3 8
8 10
12 15
13 14
1 5
输出数据 1
2
1 10
12 18
'''
n=int(input())
l=[]
m=0
for i in range(n):
    t=list(map(int,input().split()))
    m=max(m,t[1])
    l.append(t)

Ha=[0]*(m+3)
for i in range(n):
    for j in range(l[i][0],l[i][1]):#其实是在n+0.5位置上标记一个1，表示这个位置被占用
        Ha[j]=1

answer=[]
i=0
while i<len(Ha):
    if Ha[i]==1:
        j=i
        while Ha[j]==1:#在创建Ha时多留几位0，以免越界
            j+=1
        answer.append([i, j])
        i=j
    else: i+=1
print(len(answer))
for i in range(len(answer)):
    print(answer[i][0],answer[i][1])