'''
Description
电路板的水平直线上，从左向右分布着n个针脚（1,2,3，……，n），用于连接导线。

连接（p,q）表示针脚p和q之间通过一根导线相互连接，导线只允许从水平直线的下方相连。对于给定的一组连线(p1,q1),(p2,q2),...,(pn,qn)，如果能适当安排这组连线，使它们互不相交，那么称这组连线是可布线的。

当出现如图3.3.13所示的针脚相连时，则称它们是不可布线的。

img

对于给定的n个针脚和k条连线，试设计一个算法判定这组连线是否可行。

Format
Input
输入若干对连线(x,y)且x<y

Output
1.若输入的这若干对连线均没有出现相交，则输出"Yes" 2.若输入的这若干对连线有出现相交，则输出"No"

Samples
输入数据 1
2 3
6 9
4 5
3 4
输出数据 1
Yes
'''
import sys
data=[]
for line in sys.stdin.readlines():
    x,y=map(int,line.split())
    if x!=y:
        data.append([x,1,y])
        data.append([y,2,x])
data=sorted(data,key=lambda x:[x[0],-x[1],-x[2]])
# print(data)
sta=[]
i=0
while i< len(data):
    if data[i][1]==1:
        sta.append(data[i])
    elif len(sta)!=0 and data[i][2]==sta[-1][0]:
        sta.pop()
    elif data[i][0]==data[i][2]:
        i+=1
    else:
        print('No')
        exit()
    i+=1
print('Yes')