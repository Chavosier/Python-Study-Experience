# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:18:21 2026

@author: Chavosier
"""

n,m=map(int,input().split())
grid = [list(input().strip()) for _ in range(n)]
ans=grid[::]
for i in range(n):
    for j in range(m):
        q=grid[i][j]
        if q=='*':
            pass
        else:
            s=0
            for a in range(-1,2):
                for b in range(-1,2):
                    if 0<=i+a<n and 0<=j+b<m and grid[i+a][b+j]=='*':
                        s+=1
            ans[i][j]=s
for i in range(n):
    for j in range(m):
        q = ans[i][j]
        print(q,end='')
    print()