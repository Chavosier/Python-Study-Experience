import random
'''
skip list is a data structure that allows fast search within an ordered sequence of elements. 
layer maybe increase.
abandon 'build' fuction.
deduplicate skip.
separate key and value
'''
head=0
skip=[[[float('-inf'),-1,-1,'dummy']]]
records=[1]

def search(key):
    global positionkey # the record of Searching
    layer=len(skip);positionkey = []
    q=p=head;i=layer-1 #<p,q>
    while i>=0:
        while q!=-1 and skip[i][q][0]<key: # to find the list(p,q) where skip[i][q][0] is the smallest element that is bigger or equal to target
            p=q;q=skip[i][q][2]
        positionkey.append([p, q])
        if i!=0: q=p=skip[i][p][1] # to move to the next layer
        i-=1
    positionkey=positionkey[::-1]
    if q!=-1 and skip[0][q][0]==key:
        return skip[0][q][3]
    else: return None # if the target is not found, return -1
# insert data
def insert(key,value):
    global skip,records
    layer=len(skip)
    search(key) # soul
    keys=[1]+[(random.randint(0,1)) for _ in range(layer-1)]
    for i in range(layer): # do insert operation in each layer according to the keys and positionkey
        if keys[i]==1:
            skip[i].append([key,-1,positionkey[i][1],value])
            records[i]+=1
            if i!=0:
                skip[i][-1][1]=len(skip[i-1])-1
            skip[i][positionkey[i][0]][2]=len(skip[i])-1
        else: break
    if len(skip[0])!=2 and sum(keys)==len(keys) and random.randint(0,1)==1:
        layer+=1
        skip.append([  [skip[0][head][0],0,1,'dummy']  ,  [key,len(skip[layer-2])-1,-1,value]  ])
        records.append(2)
# remove data
def remove(key):
    global skip,records
    layer=len(skip)
    search(key) # soul
    for i in range(layer): # do Del operation in each layer according to the positionkey
        if positionkey[i][1]!=-1 and skip[i][positionkey[i][1]][0]==key: 
            skip[i][positionkey[i][0]][2]=skip[i][positionkey[i][1]][2]
            records[i]-=1
        else: break
    for i in range(len(records)-1,0,-1):# deduplication
        if records[i]==1 or records[i]==records[i-1]:
            records.pop(i)
            skip.pop(i)
# 
def view():
    for i in range(len(skip)):
        x=head
        while x!=-1:
            print(str(skip[i][x][0])+'('+str(skip[i][x][3])+')', end=' ')
            x=skip[i][x][2]
        print()
# debag        
# insert(1,'a')
# insert(2,'b')
# insert(4,'c')
# insert(5,'d')
# insert(6,'e')
# view()
# # print(search(3))
# remove(5)
# view()