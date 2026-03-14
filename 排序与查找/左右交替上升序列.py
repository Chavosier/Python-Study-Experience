'''
Description
列表a中存储的是左右交替上升的n个正整数序列，请你依据二分查找思想编写程序。

Format
Input
第一行，输入若干个正整数构成左右交替上升特征（数据之间用空格间隔）。

第二行，输入正整数key

Output
若key存在，则输出“YES”及二分查找次数

若key不存在，则输出“NO”

Samples
输入数据 1
2 8 15 23 33 29 17 10 5
15
输出数据 1
YES
1
'''
def Print(y):
    for i in range(len(y)):
        print(y[i])
l=list(map(int,input().split()))
key=int(input())
n=len(l)
L=0;R=(n-1)//2
num=0;f=False
while L<=R:
    mid=(L+R)//2
    num+=1
    if l[mid]==key:
        f=True
        break
    elif l[mid]>key:
        R=mid-1
    else:
        L=mid+1
if not f:
    if R>=0 and l[n-1-R]==key:
        print('YES')
        print(num+1)
    else:
        print("NO")
else:
    print('YES')
    print(num)












'''
def Print(l):
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[-1])

l_helper=list(map(int,input().split()))
key=int(input())

l1=[];l2=[]
for i in l_helper:
    if i%2==1:
        l1.append(i)
    elif i%2==0:
        l2.append(i)

x_key=key%2
if x_key==1:
    s=0
    L=0;R=len(l1)-1
    while L <= R:
        s += 1
        mid = (L + R) // 2
        if l1[mid] > key:
            R = mid - 1
        elif l1[mid] < key:
            L = mid + 1
        else:
            print('YES')
            print(s)
            exit()
    print('NO')
if x_key==0:
    s=0
    L=0;R=len(l2)-1
    while L <= R:
        s += 1
        mid = (L + R) // 2
        if l2[mid] > key:
            R = mid - 1
        elif l2[mid] < key:
            L = mid + 1
        else:
            print('YES')
            # print(s-4)
            exit()
    print('NO')
"""
40 36 30 26 22 8 4 2 1 7 13 15 21
15
"""


'''