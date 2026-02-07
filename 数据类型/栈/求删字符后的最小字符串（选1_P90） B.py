'''
Description
输入一个仅包含ASCII字符集的字符串s，现要求删除其中k（k小于字符串s的长度）个字符，使得剩余的字符在保存相对位置不变的情况下，构成一个最小的字符串。

Format
Input
第1行输入字符串s

第2行输入一个正整数k（k小于字符串s的长度）

Output
请你先删除字符串s中的k个字符，然后输出得到的最小字符串。

Samples
输入数据 1
a3b3e4c
3
输出数据 1
334c
'''
a=input()
m=int(input())
def DDD(a):
    p=len(a)-1
    for i in range(1,len(a)):
        if a[i-1]>a[i]:
            p=i-1
            break
    return(a[0:p]+a[p+1:])
for i in range(m):
    a=DDD(a)
print(a)