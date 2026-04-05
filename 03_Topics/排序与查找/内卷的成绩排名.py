'''
Description
自从实施了集星卡换奶茶的奖励措施以后，每次考试的成绩就变得特别重要，因为前n名可以获得星星（含并列）。今天，J老师公布了上一次周测中班级同学的成绩，希望你能对他们进行排名，以此确定获得星星的人选。

Format
Input
第1行为两个整数，表示学生人数m和可以获得星星的排名n（n≤m）

第2至m+1行，每行为一个学生的姓名缩写和对应的成绩。

Output
第1至m行每行为该同学的排名和姓名，按排名从小到大输出结果；若排名相同，则按姓名缩写的字典序升序排列（为了避免内卷，就不用输出成绩了）。

第m+1行为一个整数，表示可以获得星星的人数s

Samples
输入数据 1
6 3
jcw 42
sxz 48
mjx 46
cjw 46
tpx 46
tyy 45
输出数据 1
1:sxz
2:cjw
2:mjx
2:tpx
5:tyy
6:jcw
4
'''
m,n=map(int,input().split())
l=[]
for i in range(m):
    t=list(input().split())
    t[1]=int(t[1])
    l.append(t)
# print(l)

i=0
while i<m-1:
    k=i;i=m
    for j in range(m-1,k,-1):
        if l[j][1]>l[j-1][1] or l[j][1]==l[j-1][1] and l[j][0]<l[j-1][0]:
            l[j],l[j-1]=l[j-1],l[j]
            i=j

def Print(s,i):
    print(str(s)+':'+l[i][0])
Print(1,0)
re=1
s=1;i=1
while i<m:
    if l[i][1]!=l[i-1][1]:
        s=i+1
    Print(s,i)
    if s<=n:
        re+=1
    i+=1
print(re)
# print(l)
# score=[]
# s=0
# for i in range(m):
#     if i==0 or l[i][1]!=l[i-1][1]:
#         s+=1
#     score.append(s)
# s=0
# for i in range(1,m):
#     if l[i][1]==l[i-1][1]:
#         s+=1
"""
2 8 15 23 33 29 17 10 5
15
"""