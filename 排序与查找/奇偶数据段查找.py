'''
Description
有一组正整数，前面存在若干个偶数，后面全部都是奇数。若奇数序列构成升序，偶数序列构成降序，请你依据二分查找的思想编写程序。

Format
Input
第一行，若干个正整数，偶数在前，奇数在后，且偶数序列构成降序，奇数序列构成升序（数据之间用空格间隔）。

第二行，输入正整数key

Output
若key存在，则第一行输出“YES”，同时第二行输出二分查找次数

若key不存在，则输出“NO”

Samples
输入数据 1
40 36 30 26 22 8 4 2 1 7 13 15 21
17
输出数据 1
NO
'''

def Print(l):
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[-1])

l_helper=list(map(int,input().split()))
key=int(input())
if key% 2 == 0:
    key=key*(-1)

l=[]
for i in l_helper:
    if i%2==0:
        l.append(i*(-1))
    elif i%2==1:
        l.append(i)
L = 0
R = len(l) - 1
s=0
while L <= R:
    s+=1
    mid=(L+R)//2
    if l[mid]>key:
        R=mid-1
    elif l[mid]<key:
        L=mid+1
    else:
        print('YES')
        print(s)
        exit()
print('NO')
"""
40 36 30 26 22 8 4 2 1 7 13 15 21
15
"""


