'''
Description
链表指的是将需要处理的数据对象以节点的形式，通过指针串联在一起的一种数据结构。链表中的每个节点一般由数据区域和指针区域两部分构成，其中数据区域用于保存实际需要处理的数据元素，指针区域用来保存该节点相邻节点的存储地址。

给出一个数据升序排列的链表，输入一个数，若链表中某节点的值等于该数，则将该节点删除，输出删除后链表中各个节点的数据。(提示：若删除的数据不存在，则将原数据依次输出！)

Format
Input
第1行，链表节点数量n，头指针head，要删除的数key。

第2~n+1行，每行为两个数x和y。x表示节点数据区域的值，y表示节点指针区域的值。

Output
删除值为key的节点后，依次输出链表中剩余节点的数据。
'''

def Print(_):
    p=head
    while p!=-1:
        print(data[p][0],end=' ')
        p=data[p][1]


n,head,key=map(int,input().split())
data=[]
for i in range(n):
    t=list(map(int,input().split()))
    data.append(t)

p=q=head
while data[p][0]!=key and p!=-1:
    q=p#let q be the previous node of p
    p=data[p][1]
if p==head:#because the head hasn't previous node
    head=data[p][1]
    Print(head)
elif p!=-1:
    data[q][1]=data[p][1]
    Print(head)
else:
    Print(head)
