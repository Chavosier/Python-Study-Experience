l=list(map(int,input().split()))
n=len(l)
i=0
while i<n-1:
    k=i;i=n
    for j in range(n-1,k,-1):
        if l[j]>l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
            i=j