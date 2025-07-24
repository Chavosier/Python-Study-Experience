m,n=map(int,input().split())
s=[1]*(m+1)
for i in range(n):
    a,b=0,0
    a,b=map(int,input().split())
    for j in range(a-1,b):
        s[j]=0
print(sum(s))