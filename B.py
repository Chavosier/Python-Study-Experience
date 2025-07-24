n=input()
lo0=1
j0=0
def muchen(x):
    flag=True
    for l in range(i,j+1):
        if n[l]==n[j+1]:
            flag=False
            break

    return flag
for i in range(len(n)-1):#
    lo=1#changdu
    j=i#i as list`s head index,j as tail index
    while muchen(j):
        lo+=1
        j+=1
        if j==len(n)-1:#avoid index out of range
            break
    if lo>lo0:
        lo0=lo;j0=i#promise lo0,j0 is the biggest and the fronter substring
print(n[j0:j0+lo0])#not j0+lo0+1


