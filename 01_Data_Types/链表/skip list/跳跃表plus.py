import random
'''
skip list is a data structure that allows fast search within an ordered sequence of elements. 
Abandon 'build' fuction.
'''
head=0
skip=[[[float('-inf'),-1,-1]]]
# create template
books=[1,3,5,7,11,13,17]

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
# add data
def insert(skip,target):
    layer=len(skip)
    search(skip,target) # soul
    keys=[1]+[(random.randint(0,1)) for _ in range(layer-1)]
    for i in range(layer): # do Add operation in each layer according to the keys and positionkey
        if keys[i]==1:
            skip[i].append([target,-1,positionkey[i][1]])
            if i!=0: skip[i][-1][1]=len(skip[i-1])-1
            skip[i][positionkey[i][0]][2]=len(skip[i])-1
        else: break
    if len(skip[0])!=1 and sum(keys)==len(keys) and random.randint(0,1)==1:
        layer+=1;skip.append([  [skip[0][head][0],0,1]  ,  [target,len(skip[layer-2])-1,-1]  ])
    return skip
# delete data
def remove(skip,target):
    search(skip,target) # soul
    for i in range(layer): # do Del operation in each layer according to the positionkey
        if positionkey[i][1]!=-1 and skip[i][positionkey[i][1]][0]==target: 
            skip[i][positionkey[i][0]][2]=skip[i][positionkey[i][1]][2]
        else: break
    return skip
# main