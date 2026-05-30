import random
'''
skip list is a data structure that allows fast search within an ordered sequence of elements. 
'''
head=0
skip=[[[float('-inf'),-1,-1]]]
# create template
books=[1,3,5,7,11,13,17]
# build skip list
# def Build(books):
#     '''
# skip[i][j][0] is the value of the element at layer i and position j
# skip[i][j][1] is the index of the element in the previous layer (i-1) that points to the current element
# skip[i][j][2] is the index of the next element in the same layer (i) that points to the current element
#     '''
#     global layer # the number of layers in the skip list
#     skip=[];t=[i for i in books];layer=0
#     flag=True
#     while flag:
#         layer+=1
#         if t!=[]:
#             skip.append(t)
#         flag=False
#         t=[books[0]] # the first element of each layer is always the same
#         for i in skip[layer-1][1:]:
#             if random.randint(0,1)==1:
#                 t.append(i);flag=True
#         if flag and t==skip[layer-1]: # assure that the new layer is not the same as the previous layer, otherwise it will cause an infinite loop
#             layer-=1;t=[]
#     for i in range(layer): # build the skip list by adding the pointers to next elements
#         for j in range(len(skip[i])-1):
#             skip[i][j]=[skip[i][j],-1,j+1]
#         skip[i][j+1]=[skip[i][j+1],-1,-1]
#     for i in range(layer-1,0,-1): # build the connections between layers
#         for j in range(len(skip[i])):
#             for k in range(len(skip[i-1])):
#                 if skip[i-1][k][0]==skip[i][j][0]:
#                     skip[i][j][1]=k;break
#     return skip
# search target
def Search(skip,target):
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
def Add(skip,target):
    layer=len(skip)
    # if target<skip[0][head][0]:
    #     '''
    #     if the new target is smaller than the head of the skip list, 
    #     we need to update the head of the skip list to the new target, 
    #     and then consider the the ord head as the new target to be added to the skip list. (target=tt)
    #     This is because the smallest element always exits in each layer.
    #     ('head' is always 0)
    #     '''
    #     tt=skip[0][head][0]
    #     for i in range(layer):
    #         skip[i][head][0]=target
    #     target=tt
    Search(skip,target) # soul
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
def Del(skip,target):
    # flag=False
    # if target==skip[0][head][0]: # this part is similar to the Add function
    #     tt=skip[0][skip[0][head][2]][0]
    #     for i in range(layer): # a clever hack
    #         skip[i][head][0]=tt-1 # to make sure that the head of the skip list is always the smallest element, and then consider the ord head as the new target to be deleted from the skip list.
    #     flag=True
    #     target=tt
    Search(skip,target) # soul
    for i in range(layer): # do Del operation in each layer according to the positionkey
        if positionkey[i][1]!=-1 and skip[i][positionkey[i][1]][0]==target: 
            skip[i][positionkey[i][0]][2]=skip[i][positionkey[i][1]][2]
        else: break
    # if flag:
    #     for i in range(layer):
    #         skip[i][head][0]=skip[i][head][0]+1 # back
    return skip
# main
skip=Add(skip,2)
skip=Add(skip,9)
skip=Add(skip,6)
skip=Add(skip,1)
skip=Add(skip,8)
def Print(skip):
    for i in range(len(skip)):
        for j in range(len(skip[i])):
            print(skip[i][j], end=' ')
        print()
    for i in range(len(skip)):
        x=head
        while x!=-1:
            print(skip[i][x][0], end=' ')
            x=skip[i][x][2]
        print()
Print(skip)
print(Search(skip,8))
skip=Del(skip,6)
Print(skip)