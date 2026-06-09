def Print(_):
    p=head
    while p!=-1:
        print(data[p][0],end=' ')
        print(data[p][1], end=' ')
        print()
        p=data[p][1]
def next(x):
    qw=data[x][1]
    return qw

n,head=map(int,input().split())
data=[]
for i in range(n):
    t=list(map(int,input().split()))
    data.append(t)

p=q=head
while  p!=-1:
    s=data[p][1]
    q=p
    while s!=-1:
        if data[s][0]!=data[p][0]:
            q=next(q)
            s=next(s)
        else:
            data[q][1]=data[s][1]
            s=next(s)
    p=next(p)
Print(head)