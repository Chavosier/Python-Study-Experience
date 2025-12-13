'''
Description
请将一组互不相同的字符，按输入先后次序依次入栈。

现指定一个字符（该字符确保是入栈字符），请你输出所有可行的出栈序列，同时要求出栈序列的开头字符是指定字符。

Format
Input
第1行，输入一组互不相同的字符（用字符" "间隔开），这些字符按输入先后次序依次入栈。

第2行，指定一个首次出栈的字符（确保该字符来自这组字符当中）。

Output
输出所有符合要求的出栈序列。

最后一行输出出栈序列的总方案

Samples
输入数据 1
1 2 3 4 5
3
输出数据 1
3 2 1 4 5
3 2 1 5 4
3 2 4 1 5
3 2 4 5 1
3 2 5 4 1
3 4 2 1 5
3 4 2 5 1
3 4 5 2 1
8
输入数据 2
a b c d e
d
输出数据 2
d c b a e
d c b e a
d c e b a
d e c b a
4
'''
l=input().split()
k=input()
pos=0
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
for you in Stupid[:-1]:
    print(you)
print(Stupid[-1])
print(len(Stupid))