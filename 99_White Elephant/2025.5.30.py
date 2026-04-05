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


print(a)