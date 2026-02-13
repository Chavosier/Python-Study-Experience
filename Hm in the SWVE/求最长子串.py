l=input()
ans=''
def finf(l,po):
    s=''
    for i in range(po,len(l)):
        if s=='' or not(l[i] in s):
            s+=l[i]
        else:
             break
    return (len(s))
x=0
for j in range(len(l)):
    if finf(l,j)>x:
        x=finf(l,j)
        t=j
print(l[t:t+x])