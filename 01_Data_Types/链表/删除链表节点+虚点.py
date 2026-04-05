def Print(head):
    p=head
    while p!=-1:
        print(data[p][0],end=' ')
        p=data[p][1]
def next(x):
    return data[x][1]

n,head,key=map(int,input().split())
data=[]
for i in range(n):
    t=list(map(int,input().split()))
    data.append(t)

data.append(['@',head])
p=head;q=len(data)-1
while p!=-1 and data[p][0]!=key:
    q=p#let q be the previous node of p
    p=next(p)
if p!=-1:
    data[q][1]=next(p)
    Print(data[-1][1])
else:
    Print(data[-1][1])
