import random
# by 阮乘雷
Maxn=30
books=[0]*Maxn
books[0]=3
for i in range(1,Maxn):
    books[i]=books[i-1]+random.randint(1,5)
print(books)
step_list=[1]
while step_list[-1]*2<Maxn:
    step_list.append(step_list[-1]*2)
print(step_list)
def delete(skip, target):
    t=p=0
    for i in range(len(skip)-1, -1, -1):
        q=skip[i][p][2]  # <t, p, q>
        while q!=-1 and skip[i][q][0]<=target:
            t=p
            p=q
            q=skip[i][p][2]
        y=skip[i][t][1]
        if skip[i][p][0]==target:
            if p==0:
                if skip[i][p][2]==-1:
                    skip.pop(i)
                else:
                    skip[i][p]=skip[i][q]
            else:
                skip[i][t][2]=skip[i][p][2]
        p=y
    return
def instill(skip,target):
    layer=0
    key=0
    while layer<len(skip) and key==0:
        forward=-1
        k=[target,forward,-1]
        skip[layer].append(k)
        j=len(skip[layer])-1
        key=random.randint(0,1)
        t = p = 0
        for i in range(len(skip) - 1, layer-1, -1):
            q = skip[i][p][2]  # <t, p, q>
            while q != -1 and skip[i][q][0] <= target:
                t = p
                p = q
                q = skip[i][p][2]
        skip[layer][j][2]=skip[layer][p][2]
        skip[layer][p][2]=j
        forward=j
        layer+=1
    return



def build_skip(books, step_list):
    n=len(books)
    layers=len(step_list)
    skip=[[] for i in range(layers)]
    for i in range(layers):
        skip[i].append([books[0], -1, -1])
        step=step_list[i]
        t=0
        for j in range(step, n, step):
            node=[books[j], -1, -1]
            skip[i].append(node)
            skip[i][t][2]=len(skip[i])-1
            t=len(skip[i])-1
        skip[i][t][2]=-1
    for i in range(layers-1, 0, -1):
        p1=0
        p2=0
        while p2!=-1:
            if skip[i][p2][0]==skip[i-1][p1][0]:
                skip[i][p2][1]=p1
                p2=skip[i][p2][2]
            p1=skip[i-1][p1][2]
    return skip


skip=build_skip(books, step_list)
print(skip)
target=3
def search_skip(skip, target):
    p=0
    for i in range(len(skip)-1, -1, -1):
        q=skip[i][p][2]  # <p, q>
        while q!=-1 and skip[i][q][0]<=target:
            p=q
            q=skip[i][p][2]
        if skip[i][p][0]==target:
            return True
        p=skip[i][p][1]
    return False
def Print(skip):
    p=0
    for i in range(len(skip)-1, -1, -1):
        print(i,end="     ")
        while p!=-1:
            print(skip[i][p],end=",")
            p=skip[i][p][2]
        print()
        p=0
    return
result=search_skip(skip, target)
print(result)
Print(skip)

delete(skip,books[29])
instill(skip,books[29]+0.5)
print(skip)
Print(skip)