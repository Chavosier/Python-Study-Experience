'''
Description
给出若干个区间，每个区间可由一个左端点和右端点组成，要求实现区间的合并。

Format
Input
第 
1
1 行为区间个数 
n
n，n≤5000

第 
2
2 行开始直至 
n
+
1
n+1 行，每行两个整数，表示每个区间的左端点和右端点

Output
第 
1
1 行为合并后的区间个数 
m
m 第 
2
2 行开始直至 
m
+
1
m+1 行，每行两个整数，表示合并后每个区间的左端点和右端点

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
def Print(y):
    for i in range(len(y)):
        print(y[i])


n=int(input())
l=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)

i=0
while i<n-1:
    k=i;i=n
    for j in range(n-1,k,-1):
        if l[j][0]<l[j-1][0]:
            l[j],l[j-1]=l[j-1],l[j]
            i=j

ans=[]
i=1
start=l[0][0]
last=l[0][1]
while i<=n-1:
    if l[i][0]<=last:
        last=max(l[i][1],last)
    else:
        ans.append(str(start)+' '+str(last))
        start=l[i][0]
        last = l[i][1]
    i+=1
t=str(start)+' '+str(last)
if t not in ans:
    ans.append(t)
# print(ans)
print(len(ans))
Print(ans)