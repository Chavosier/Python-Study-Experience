n,k=map(int,input().split())
d=[0]+list(map(int,input().split()))
s=[0]*(n+1)
for i in range(1,n+1):
    s[i]=s[i-1]+d[i]
que=[-1]*(n+2)
head=0;tail=0
minl=[0]
for i in range(1,n+1):
    if head<tail and que[head]+k<=i:
        head+=1
    while head<tail and s[que[tail-1]]>=s[i]:
        tail-=1
    que[tail]=i
    tail+=1
    minl.append(s[que[head]])
maxt=s[k]-s[0]
for i in range(1,n+1):
    maxt=max(maxt,s[i]-minl[i-1])
print(maxt)