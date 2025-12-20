import random
n=3
flag=[False]*(n*n+1)
a=[[0 for i in range(n)]for j in range(n)]
i=0
while i<n:
    j=0
    while j<n:
        a[i][j]=random.randint(1,n*n)
        if flag[a[i][j]]==False:
            flag[a[i][j]]=True
            j+=1
    i+=1
for i in range(n):
    print(a[i])
def check(x):
    row=(x-1)//n
    col=(x-1)%n
    if row%2==1:
        col=n-col-1
    return a[row][col]
for i in range(1,n*n+1):
    print(check(i))