import random
head=0
Maxn=10;books=[0]*Maxn;books[0]=3
for i in range(1,Maxn):
    books[i]=books[i-1]+random.randint(1,5)
def Build(books):
    global layer
    skip=[];t=[i for i in books];layer=0
    flag=True
    while flag:
        layer+=1
        if t!=[]:
            skip.append(t)
        flag=False
        t=[books[0]]
        for i in skip[layer-1][1:]:
            if random.randint(0,1)==1:
                t.append(i);flag=True
        if flag and t==skip[layer-1]:
            layer-=1;t=[]
    for i in range(layer):
        for j in range(len(skip[i])-1):
            skip[i][j]=[skip[i][j],-1,j+1]
        skip[i][j+1]=[skip[i][j+1],-1,-1]
    for i in range(layer-1,0,-1):
        for j in range(len(skip[i])):
            for k in range(len(skip[i-1])):
                if skip[i-1][k][0]==skip[i][j][0]:
                    skip[i][j][1]=k;break
    return skip
def Search(skip,target):
    global positionkey
    positionkey = []
    q=p=head;i=layer-1
    while i>=0:
        while q!=-1 and skip[i][q][0]<target:
            p=q;q=skip[i][q][2]
        positionkey.append([p, q])
        if i!=0: q=p=skip[i][p][1]
        i-=1
    positionkey=positionkey[::-1]
    if skip[i+1][q][0]==target:
        return q
    else: return -1
def Add(skip,target):
    if target<<skip[0][head][0]:
        tt=skip[0][head][0]
        for i in range(layer):
            skip[i][head][0]=target
        target=tt
    Search(skip,target)
    keys=[1]+[(random.randint(0,1)) for _ in range(layer-1)]
    for i in range(layer):
        if keys[i]==1:
            skip[i].append([target,-1,positionkey[i][1]])
            if i!=0: skip[i][-1][1]=len(skip[i-1])-1
            skip[i][positionkey[i][0]][2]=len(skip[i])-1
        else: break
    return skip
def Del(skip,target):
    flag=False
    if target==skip[0][head][0]:
        tt=skip[0][skip[0][head][2]][0]
        for i in range(layer):
            skip[i][head][0]=tt-1
        flag=True
        target=tt
    Search(skip,target)
    for i in range(layer):
        if positionkey[i][1]!=-1 and skip[i][positionkey[i][1]][0]==target:
            skip[i][positionkey[i][0]][2]=skip[i][positionkey[i][1]][2]
        else: break
    if flag:
        for i in range(layer):
            skip[i][head][0]=skip[i][head][0]+1
    return skip
skip=Build(books)
