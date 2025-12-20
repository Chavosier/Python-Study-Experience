n=int(input())
m=list(map(int,input().split()))
def muchen(x):
    flag=True
    if m[x] >= m[x + 1]:
        flag = False

    # for l in range(i,j+1):
    #     if m[l]>=m[j+1]:
    #         flag=False
    #         break
    return flag
lo0=1
for i in range(n-1):#
    lo=1#changdu
    j=i#i as list`s head index,j as tail index
    while muchen(j):
        lo+=1
        j+=1
        if j==n-1:#avoid index out of range
            break
    if lo>lo0:
        lo0=lo#promise lo0,j0 is the biggest and the fronter substring
print(lo0)#not j0+lo0+1


