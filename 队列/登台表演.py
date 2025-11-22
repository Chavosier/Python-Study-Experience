'''
Description
为了让全班同学参加文艺汇演，小王设计了一个节目：

先让 k 个同学同时出现在舞台上开始表演，当某1个同学率先完成他的表演部分，马上离开舞台，第k+1个同学会立即出现在舞台上并开始表演；当第2个同学离开舞台时，第k+2个同学也随即出现在舞台……

以此类推，直到所有同学上台，当最后一个同学完成他舞台上的表演，节目结束。方法如下：

①前k个人一开始就登录舞台，这k个人离开舞台的时刻等同于各自舞台上的表演时长。

②当舞台有人离开后，后面登录舞台的同学，他离开舞台时刻是他的表演时长+他之前离开舞台同学的时刻和。

由于表演时长有限，小王希望在表演限定时长tmax内，确定最少在舞台上同时表演的同学数量k。

Format
Input
第 1 行共有若干个正整数，每个正整数代表学生本次表演的时长，中间用空格间隔开。

第 2 行一个正整数：tmax（tmax代表本次表演限定表演时长）

Output
在限定时间tmax范围时间内，若所有同学都完成表演，请你求出在舞台上同时表演的最少学生数k。

（1）找到，则输出k

（2）找不到，则输出-1

Samples
输入数据 1
20  40  15  25  10  30
60
输出数据 1
3
Limitation
1s, 1024KiB for each test case.

说明：本题可使用优先队列，每次入队时选择队列中首个结束的队伍加入。（参考教材P81）'''
from queue import PriorityQueue
d=list(map(int,input().split()))
n=len(d)
tmax=int(input())
def check(k):
    que=PriorityQueue()
    for i in range(k):
        que.put(d[i])
    for i in range(k,n):
        tim=que.get()+d[i]
        que.put(tim)
    while not que.empty():
        ans=que.get()
    return ans<=tmax
if tmax<max(d):
    print(-1)
else:
    for k in range(1,n+1):
        if check(k):
            print(k);break