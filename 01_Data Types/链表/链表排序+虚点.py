'''
Description
链表指的是将需要处理的数据对象以节点的形式，通过指针串联在一起的一种数据结构。链表中的每个节点一般由数据区域和指针区域两部分构成，其中数据区域用于保存实际需要处理的数据元素，指针区域用来保存该节点相邻节点的存储地址。

给出一个链表，请输出按升序排序后链表中各个节点的数据信息。

Format
Input
第1行，链表节点数量n和头指针head。

第2~n+1行，每行为两个数x和y。x表示节点数据区域的值，y表示节点指针区域的值。

Output
通过对链表升序处理后，依次输出链表中各个节点的数据信息。

5 2
10 3
30 4
40 1
50 -1
70 0

'''
def Print(head):
    o=head
    while o!=-1:
        print(data[o][0],end=' ')
        print(data[o][1])
        o=data[o][1]

n,head=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
data.append(['@',head])
dummy=len(data)-1
#Print(head)
x=data[head][1]
data[head][1]=-1
while x!=-1:
    t=data[x][1]#储存x的后继
    q=dummy
    p=head
    while p!=-1 and data[x][0]>data[p][0]:
        q=p
        p=data[p][1]
    data[x][1]=p
    data[q][1]=x
    x=t
    head=data[dummy][1]
Print(head)