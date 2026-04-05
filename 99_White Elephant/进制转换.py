n,k=map(int,input().split())
z='0123456789ABCDEF'
cnt=0
for i in range(1,n+1):
    m=i
    s=''
    while m>0:
        s=z[m%k]+s
        m//=k
print(s)
