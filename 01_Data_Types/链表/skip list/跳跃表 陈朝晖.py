from random import randint
Maxn=3;  Maxm=10
Data=[0]*(Maxn+Maxm)
Next=[[-1]for i in range(Maxn+Maxm)]
def Print(lev):
    print('lev=%d:' %lev)
    p=Next[lev][0]
    while p!=-1:
        print(Data[p], end=',')
        p=Next[p][lev]
    print()
def Create():
    Next[0][0]=Maxn
    Data[Maxn]=randint(1,3)
    for i in range(Maxn+1, Maxm):
        Data[i]=Data[i-1]+randint(1,3)
        Next[i-1][0]=i
    Print(0)
    for lev in range(1, Maxn):
        p=Next[lev-1][0]
        q=-1
        while p!=-1:
            t=randint(0,1)
            if t==1:
                Next[p].append(-1)
                if q==-1:
                    Next[lev][0]=p
                else:
                    Next[q][lev]=p
                q=p
            p=Next[p][lev-1]
        Print(lev)
Create()




# import random
# Maxn=30
# books=[0]*Maxn
# books[0]=3
# for i in range(1,Maxn):
#     books[i]=books[i-1]+random.randint(1,5)
# print(books)
# step_list=[1]
# while step_list[-1]*2<Maxn:
#     step_list.append(step_list[-1]*2)
# print(step_list)

# def build_skip(books, step_list):
#     n=len(books)
#     layers=len(step_list)
#     skip=[[] for i in range(layers)]
#     for i in range(layers):
#         skip[i].append([books[0], -1, -1])
#         step=step_list[i]
#         t=0
#         for j in range(step, n, step):
#             node=[books[j], -1, -1]
#             skip[i].append(node)
#             skip[i][t][2]=len(skip[i])-1
#             t=len(skip[i])-1
#         skip[i][t][2]=-1
#     for i in range(layers-1, 0, -1):
#         p1=0
#         p2=0
#         while p2!=-1:
#             if skip[i][p2][0]==skip[i-1][p1][0]:
#                 skip[i][p2][1]=p1
#                 p2=skip[i][p2][2]
#             p1=skip[i-1][p1][2]
#     return skip


# skip=build_skip(books, step_list)
# target=17
# def search_skip(skip, target):
#     p=0
#     for i in range(len(skip)-1, -1, -1):
#         q=skip[i][p][2]  # <p, q>
#         while q!=-1 and skip[i][q][0]<=target:
#             p=q
#             q=skip[i][p][2]
#         if skip[i][p]==target:
#             return True
#         p=skip[i][p][1]
#     return False
# result=search_skip(skip, target)