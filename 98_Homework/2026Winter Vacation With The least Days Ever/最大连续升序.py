m=input()
l=list(map(int,input().split()))
ans=1
for i in range(len(l)-1):
    s=1
    j=i+1
    while j<len(l):
        if l[j]>l[j-1]:
            s+=1
        else:
            break
        j+=1
    if s>ans:
        ans=s
print(ans)