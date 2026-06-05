import random
'''
skip list is a data structure that allows fast search within an ordered sequence of elements. 
Abandon 'build' fuction.
'''
head=0
skip=[[[float('-inf'),-1,-1]]]
records=[1]

def search(skip,target):
    global positionkey,layer # the record of Searching
    layer=len(skip);positionkey = []
    q=p=head;i=layer-1 #<p,q>
    while i>=0:
        while q!=-1 and skip[i][q][0]<target: # to find the list(p,q) where skip[i][q][0] is the smallest element that is bigger or equal to target
            p=q;q=skip[i][q][2]
        positionkey.append([p, q])
        if i!=0: q=p=skip[i][p][1] # to move to the next layer
        i-=1
    positionkey=positionkey[::-1]
    if skip[i+1][q][0]==target:
        return q
    else: return -1 # if the target is not found, return -1
# insert data
def insert(skip,target):
    layer=len(skip)
    search(skip,target) # soul
    keys=[1]+[(random.randint(0,1)) for _ in range(layer-1)]
    for i in range(layer): # do insert operation in each layer according to the keys and positionkey
        if keys[i]==1:
            skip[i].append([target,-1,positionkey[i][1]])
            records[i]+=1
            if i!=0:
                skip[i][-1][1]=len(skip[i-1])-1
            skip[i][positionkey[i][0]][2]=len(skip[i])-1
        else: break
    if len(skip[0])!=1 and sum(keys)==len(keys) and random.randint(0,1)==1:
        layer+=1
        skip.append([  [skip[0][head][0],0,1]  ,  [target,len(skip[layer-2])-1,-1]  ])
        records.append(2)
    return skip
# remove data
def remove(skip,target):
    search(skip,target) # soul
    for i in range(layer): # do Del operation in each layer according to the positionkey
        if positionkey[i][1]!=-1 and skip[i][positionkey[i][1]][0]==target: 
            skip[i][positionkey[i][0]][2]=skip[i][positionkey[i][1]][2]
            records[i]-=1
        else: break
    for i in range(len(records)-1,0,-1):
        if records[i]==1 or records[i]==records[i-1]:
            records.pop(i)
            skip.pop(i)
    return skip
# main
def Print(skip):
    for i in range(len(skip)):
        x=head
        while x!=-1:
            print(skip[i][x][0], end=' ')
            x=skip[i][x][2]
        print()
skip=insert(skip,2)
skip=insert(skip,9)
skip=insert(skip,6)
skip=insert(skip,1)
skip=insert(skip,8)
Print(skip)
skip=remove(skip,8)
Print(skip)