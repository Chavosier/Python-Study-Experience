'''
题目描述
设有 
n
n 个活动的集合 
E
=
{
1
,
2
,
.
.
,
n
}
E={1,2,..,n}，其中每个活动都要求使用同一资源，如演讲会场等，而在同一时间内只有一个活动能使用这一资源。每个活动 
i
i 都有一个要求使用该资源的起始时间 
s
i
s 
i
​
  和一个结束时间 
f
i
f 
i
​
 ，且 
s
i
<
f
i
s 
i
​
 <f 
i
​
 。如果选择了活动 
i
i ，则它在时间区间 
[
s
i
,
f
i
)
[s 
i
​
 ,f 
i
​
 ) 内占用资源。若区间 
[
s
i
,
f
i
)
[s 
i
​
 ,f 
i
​
 ) 与区间 
[
s
j
,
f
j
)
[s 
j
​
 ,f 
j
​
 ) 不相交，则称活动 
i
i 与活动 
j
j 是相容的。也就是说，当 
f
i
≤
s
j
f 
i
​
 ≤s 
j
​
  或 
f
j
≤
s
i
f 
j
​
 ≤s 
i
​
  时，活动 
i
i 与活动 
j
j 相容。选择出由互相兼容的活动组成的最大集合。

输入格式
第一行一个整数 
n
n；

接下来的 
n
n 行，每行两个整数 
s
i
s 
i
​
  和 
f
i
f 
i
​
 。

输出格式
输出互相兼容的最大活动个数。

样例
输入数据 1
4
1 3
4 6
2 5
1 7
输出数据 1
2
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