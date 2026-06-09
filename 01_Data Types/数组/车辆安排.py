# Description
# 某会务组根据参会者提交的入住宾馆和到达指定上车点时间的信息，安排车辆接送参会者去宾馆。
# 不同宾馆的参会者分开接送，同一宾馆的参会者可同乘一辆车，每辆车最多接送v人，
# 每个参会者的等待时间都不超过w分钟。
# 参会者入住的宾馆和到达上车点的时间用长度为7的字符串表示，例如A-09:15表示参会者当天入住A宾馆，9点15分到达上车点。
# 如果w为10，那么该参会者最晚9点25分出发去宾馆。
# 编写程序，统计接送n个参会者所需的最少车辆数。

# Format
# Input
# 第一行为三个整数 n (1⩽n⩽1000), v (4⩽v⩽30), w (5⩽w⩽60)。
# 接下来n行，每行为参会者入住的宾馆和到达上车点的时间，是长度为7的字符串；

# Output
# 输出所需的最少车辆数。


#这种思路用pop删除列表前面的元素来模拟车辆的接送
# 由于pop(0)的时间复杂度是O(n)，所以这种方法在数据量大的时候会超时
n,v,w=map(int,input().split())

d={}
for _ in range(n):
    s=input()
    h,m=map(int,s[2:].split(':'))
    t=h*60+m
    if s[0] not in d:
        d[s[0]]=[]
    d[s[0]].append(t)
an=0
for i in d:
    d[i].sort()
    while len(d[i])>0:
        #通过删除列表前面的元素来模拟车辆的接送
        for j in range(len(d[i])):
            if d[i][j]>d[i][0]+w:
                j-=1
                break
            if j==v-1:
                break
        for k in range(j+1):
            d[i].pop(0)
        # if j==0:
        #     d[i].pop(0)
        an+=1
print(an)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# 另一种思路是通过排序后遍历列表来模拟车辆的接送
# 这种方法的时间复杂度是O(nlogn)，不会超时
n, v, w = map(int, input().split())
a = []
for i in range(n):
    s1 = input()
    a.append(s1)

a.sort()
num = 1        # num用于记录总共派的车辆数量
cnt = 1        # cnt用于存储当前这辆车上的人数
tp = a[0][0]   # tp用于标记这辆车的宾馆类型
tm = int(a[0][2:4]) * 60 + int(a[0][5:])  # 第一个人的到达时间（分钟）
Last = tm + w  # Last用于记录这辆车最迟上次时间

for i in range(1, n):
    tp2 = a[i][0]
    tm2 = int(a[i][2:4]) * 60 + int(a[i][5:])
    if tp2 != tp or tm2 > Last or cnt >= v:#判定是否换车
        num += 1
        tp = tp2
        Last = tm2 + w
        cnt = 1
    else:
        cnt+=1
print(num)