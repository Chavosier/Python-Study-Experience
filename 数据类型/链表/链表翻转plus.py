'''
Description
第1行输入一个整数n和head（表示该单链表共有n个节点，链表头指针是head）

第2行，输入两个正整数x,y（1<=x<=y<=n）

第3至n+2行，每行输入一个单链表节点的相关信息

要求将该单链表中[x..y]之间的所有节点进行翻转，输出翻转后的单链表

Format
Input
第1行，链表节点数量n和头指针head。

第2~n+1行，每行为两个数x和y。x表示节点数据区域的值，y表示节点指针区域的值。

Output
遍历单链表中的n个节点，输出共n行，依次输出各个节点信息，

Samples
输入数据 1
5 2
2 4
40 3
20 4
10 1
50 -1
30 0
输出数据 1
10 0
40 4
30 1
20 3
50 -1
Limitation
1s, 1024KiB for each test case.
'''
def Print(head):
    p=head
    while p!=-1:
        print(data[p][0],end=' ')
        print(data[p][1])
        p=data[p][1]

n,head_o=map(int,input().split())
a,b=map(int,input().split())
data=[]
for i in range(n):
    t=list(map(int,input().split()))
    data.append(t)

s=0
q=head_o
pa=head_o;pb=head_o
while q!=-1:
    s+=1
    if s==a:
        pa=q
    if s==b:
        pb=q
    q=data[q][1]
head=pa
data[pb][1]=-1

p=data[head][1]
data[head][1]=-1
