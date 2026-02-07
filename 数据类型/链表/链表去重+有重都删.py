'''
Description
链表指的是将需要处理的数据对象以节点的形式，通过指针串联在一起的一种数据结构。链表中的每个节点一般由数据区域和指针区域两部分构成，其中数据区域用于保存实际需要处理的数据元素，指针区域用来保存该节点相邻节点的存储地址。

给出一个链表，若链表中存在两个或两个以上的节点数据区域值相同，则将链表中所有等于该数据区域值节点删除。

输出删除后链表中各个节点的数据信息。(提示：若所有数据区域值均不重复，则将原链表信息依次输出！)

Format
Input
第一行，链表节点数量n，头指针head。 第2~n+1行，每行为两个数x和y。x表示节点数据区域的值，y表示节点指针区域的值。

Output
删除链表中数据区域值相同节点后，依次输出链表中剩余节点的数据信息。

若该链表中所有数据区域值均有重复，则输出"None"
'''
def Print(_):
    p=head
    while p!=-1:
        print(data[p][0],end=' ')
        print(data[p][1])
        p=data[p][1]
def next(x):
    qw=data[x][1]
    return qw

n,head=map(int,input().split())
data=[]
for i in range(n):
    t=list(map(int,input().split()))
    data.append(t)
data.append(['@',head])
dummy=len(data)-1
d=dummy
p=q=head
while  p!=-1:                       #p为当前节点，为判断重复的基准
    s=data[p][1]                    #s从p的下一个节点开始，以while语句判断是否有重复
    q=p                             #q为s的前一个节点
    flag_none=True                  #判断是否没有重复
    while s!=-1:
        if data[s][0]!=data[p][0]:
            q=next(q)
            s=next(s)
        else:
            data[q][1]=data[s][1]
            s=next(s)
            flag_none=False
    t=next(p)                       #后面可能删除p节点，所以先保存p的下一个节点
    if not flag_none:
        data[d][1]=t                #删除p节点，将d节点指向p的下一个节点
    else:
        d=next(d)                   #没有重复，d后移
    p=t                             #p后移，回收存贮的p的下一个节点
head=data[dummy][1]                 #更新head
if head!=-1:
    Print(head)
else:
    print('None')