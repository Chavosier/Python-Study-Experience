def shuff(data,c):
    m=len(c)
    s=[0]*m
    k=0
    while k<len(data):
        for i in range(m):
            s[i]=data[k+i]
        for i in range(m):
            data[k+i]=s[c[i]]
        k+=m
def compare(data,i,r):
    j=0
    while j<len(r) and i+j<len(data):
        if r[j]!=data[i+j]:
            break
        else:
            j+=1
    return j
def trans(data,r,segs):
    newsegs=[]
    for s in segs:
        if s[0]==0:
            h=i=s[1]
            m=len(r)
            while i+m <= s[2]+1:
                if compare(data,i,r)==m:
                    if i>h:
                        newsegs.append([0,h,i-1])
                    newsegs.append([1,i,i+m-1])
                    i+=m
                    h=i
                else:
                    i+=1
            if h<=s[2]:
                newsegs.append([0,h,s[2]])
        else:
            newsegs.append(s)
    return newsegs
def update(data,segs):
    for s in segs:
        if s[0]!=0:
            data.append(0)
    p=len(data)-1
    for i in range(len(segs)-1,-1,-1):
        for j in range(segs[i][2],segs[i][1]-1,-1):
            data[p]=data[j]+segs[i][0]
            p-=1
        if segs[i][0]>0:
            data[p]=127+segs[i][0]
            p-=1

