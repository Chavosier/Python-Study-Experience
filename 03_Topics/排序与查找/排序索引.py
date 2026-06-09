# -*- coding: utf-8 -*-

l=list(map(int,input().split()))
n=len(l)

index=[i for i in range(n)]
for i in range(n-1):
    for j in range(n-i-1):
        if l[index[j]]>=l[index[j+1]]:
            index[j],index[j+1]=index[j+1],index[j]
print(index)
