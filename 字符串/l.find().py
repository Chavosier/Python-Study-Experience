def find(l,k):
    a=-1
    if len(l)<len(k):
        return a
    for i in range(len(l)-len(k)+1):
        s=[-1]
        for j in range(len(k)):
            if l[i+j]==k[j]:
                s.append(0)
            else:
                s.append(1)
                break
        if sum(s)==-1:
            a=i
            return a
    return a
l='f'
k='fs'
a=find(l,k)
print(a)