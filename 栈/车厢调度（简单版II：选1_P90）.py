'''
Description
栈结构的火车调度站如下图所示，每节火车车厢从入口驶入，经栈结构的车站后可以重新组合，然后从出口驶出。

img

现有n节硬席和软席车厢（分别以H和S表示），依次从入口驶入，出口驶出时将所有的软席车厢调度到硬席车厢之前。

例如，编组为“HSHHS”的车厢组合经调度后变为“SSHHH”。请你编写一个程序，输出调度时的操作序列。

Format
Input
输入一行字符串，表示调度前的火车车厢序列（硬席和软席车厢分别以H和S表示）

Output
输出调度时的操作序列，要求该操作序列数量最少。具体操作如： 1.Push H 2.Push S 3.Pop S …… ……

Samples
输入数据 1
HSHHS
输出数据 1
1.Push H
2.Push S
3.Pop S
4.Push H
5.Push H
6.Push S
7.Pop S
8.Pop H
9.Pop H
10.Pop H
'''
l=input()
i=0
s=0
while i<len(l):
    s+=1
    if l[i]=='H':
        print(str(s)+'.Push H')
    elif l[i]=='S':
        print(str(s) + '.Push S')
        s+=1
        print(str(s) + '.Pop S')
    i+=1
j=0
while j<len(l):
    if l[j]=='H':
        s+=1
        print(str(s)+'.Pop H')
    j+=1