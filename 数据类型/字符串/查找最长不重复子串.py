'''
Description
重复子串指的是：一个字符串的子串中可能含有重复出现的字符，如字符串“abab”的其中一个子串“aba”就含有2个重复出现的字符“a”。请编写程序找出给定字符串中最长不重复子串，如果存在多个，则按其出现先后次序将其输出，每行一个。

Format
Input
一行字符串

Output
可能多行，每行一个最长子串 若存储母串中存在多个最长子串，则按子串在母串中的先后次序依次输出，每行一个子串。 所有输出的不重复子串要求长度最长，同时输出的子串均不相同。

Samples
输入数据 1
abab
输出数据 1
ab
ba
'''

l=input()
def check(i):
    s=''
    m=0
    for j in range(i,len(l)):
        if l[j] not in s:
            s+=l[j];m+=1
        else:
            return [s,m]
    return [s,m]

max=0
ans=[]
for i in range(len(l)):
    qw=check(i)
    # print(qw)
    q=qw[0]
    w=qw[1]
    if w>max:
        max=w
        ans=[]
        if q not in ans:
            ans.append(q)
    elif w==max:
        if q not in ans:
            ans.append(q)
for k in ans:
    print(k)



