'''
Description
已知A国人有n个人，B国人有m个人， A国人和B国人手拉手围成一圈（圈编号是1至n+m），从第1个人开始按顺时针次序报数，报到10的这个人将会出圈。

然后下一个人从1开始重新报数，按上述方法若干次出圈后，圈内剩下的全部都是A国人。

请问A国人和B国人应该如何排列？

Format
Input
输入数据共一行，两个正整数n和m，分别代表A国人和B国人的人数。

Output
输出共两行，第1行按出圈次序输出B国人的出圈编号。 第2行输出圈内A国人的编号。

（说明：B国人编号按实际出圈次序输出，A国人的编号按从小到输出。）

5 3 


2 5 1
3 4 6 7 8

'''

def Print(head):
    p=head
    for _ in range(n):
        print(data[p][0],end=' ')
        p=data[p][1]

n,m=map(int,input().split())
data=[]
for i in range(m+n):
    data.append([i+1,i+1])
data[len(data)-1][1]=0
head=0
dummy=len(data)-1
m_=0
cur=pre=head
t=1
while m_!=m :
    if t!=10:
        pre=cur
        cur=data[cur][1]
        t+=1
    else:
        t=1
        q=data[pre][1]
        data[pre][1]=data[cur][1]
        print(data[cur][0],end=' ')
        if cur==head:
            head=data[cur][1]
        pre=q
        cur=data[cur][1]
        m_+=1
print()
Print(head)