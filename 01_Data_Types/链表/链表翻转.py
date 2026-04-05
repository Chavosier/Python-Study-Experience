'''
Description
输入一个含n个节点单链表的相关信息。

将该单链表进行翻转，依次输出翻转后的单链表节点信息。

Format
Input
第1行，输入单链表节点数量n和头指针head。

第2~n+1行，每行输入两个整数x和y。x表示节点数据区域的值，y表示节点指针区域的值。

Output
输出共n行，每行输出单链表中各节点信息。
'''
n,head=map(int,input().split())
data=[]
for i in range(n):
    t=list(map(int,input().split()))
    data.append(t)

p=data[head][1]
data[head][1]=-1
while p!=-1:
    t=data[p][1]
    data[p][1]=head
    head=p
    p=t

p=head
while p!=-1:
    print(data[p][0],end=' ')
    print(data[p][1])
    p=data[p][1]
