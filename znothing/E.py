def E(x):#检测移到哪个位置
    for i in range(1,x):
        if l[i-1]<=l[x]<l[i]:#< and <=
            s=i
            break
        else:
            s=x
    return s
def F(y):#move到x位置
    z=l[y]
    e=E(y)
    for j in range(y-1,e-1,-1):
        l[j+1]=l[j]
    l[e]=z
    ot=y-e
    return l,ot

ot2=0
n=int(input())
l=list(map(int,input().split()))
l=[0]+l

for i in range(2,n+1):
    f=F(i)
    l=f[0]
    ot2+=f[1]

l=l[1:]
print(' '.join(map(str, l)))
print(ot2)
