'''
Description
栈是常用的一种数据结构，有n个元素在栈顶端一侧等待进栈，栈顶端另一侧是出栈序列。你已经知道栈的操作有两种：push和pop，前者是将一个元素进栈，后者是将栈顶元素弹出。现在要使用这两种操作，由一个操作序列可以得到一系列的输出序列。

请你编程求出对于给定的n，计算并输出由操作数序列1,2,...,n，经过一系列操作可能得到的输出序列总数。

Format
Input
输入两个正整数n，k(1<=n<=1000，n表示n个元素，k表示栈的大小k<=n)。

Output
输出若干行，每行给出可能的出栈序列。

最后一行，输出可行的出栈序列总数量。

Samples
输入数据 1
3 2
输出数据 1
1 2 3
1 3 2
2 1 3
2 3 1
4
'''
s=0
pos=0
n,topmax=map(int,input().split())
topmax-=1
ll=[str(i+1) for i in range(n)]
def check(x):
    x=x.split()
    mtop=0
    sta=[];top=-1
    p=0;i='1'
    while i!=str(n+1):
        if top==-1 or sta[top]<x[p]:
            sta.append(i);top+=1;i=str(int(i)+1)
            mtop=max(mtop,top)
        elif top!=-1 and sta[top]==x[p]:
            p+=1
            sta.pop();top-=1
        else:
            sta.pop();
            top -= 1
    return mtop<=topmax

for k in ll:
    l=ll.copy()
    for i in range(len(l)):
        if l[i]==k:
            pos=i
            break
    def Out(l,pos):
        l=l.copy()
        n=len(l);R=[]
        ways=[-1]+[i for i in range(n-pos-1)]
        r=l.pop(pos)
        if len(l)==0:
            R.append(r)
        else:
            for way in ways:
                if pos+way!=-1:
                    pos0=pos+way
                    A=Out(l,pos0)
                    for a in A:
                        R.append(r+' '+a)


        return R
    Stupid=Out(l,pos)
    for you in Stupid:
        if check(you):
            print(you)
            s+=1
print(s)
# topmax=1
# n=3
# def check(x):
#     x=x.split()
#     mtop=0
#     sta=[];top=-1
#     p=0;i='1'
#     while i!=str(n+1):
#         if top==-1 or sta[top]<x[p]:
#             sta.append(i);top+=1;i=str(int(i)+1)
#             mtop=max(mtop,top)
#         elif top!=-1 and sta[top]==x[p]:
#             p+=1
#             sta.pop();top-=1
#         else:
#             sta.pop();
#             top -= 1
#     return mtop<=topmax
# print(check('3 2 1'))