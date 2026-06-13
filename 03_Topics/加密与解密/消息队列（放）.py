# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:46:06 2026

@author: Chavosier & Kimi
"""

'''
E. 消息队列（放）P78

Description
给定一个字符串S1,S2,...,Sn，按如下规则加密：
（1）取第一个字符S1，将第二个字符S2放到字符串末尾Sn后面，得到字符串S3...SnS2...
（2）然后将S3取出，将S4放到末尾S2后面...
（3）重复步骤（1）（2）...
直到最后一个字符Sn被取出，这些字符按取出顺序形成一个新的字符串，称为密文。

请编写一个程序，输入一个字符串s（长度不超过30），输出该字符串的密文。

Format
Input
一行字符串s，要求对该字符串s进行加密，得到密文ans
Output
输出密文ans

Samples
Python
Ptoynh

Limitation
1s, 1024KiB for each test case.
'''

l=input()
k=1
r=''
i=0
while len(l)!=0:
    if k==1:
        r+=l[0]
        l=l[1:]
    else:
        p=l[0]
        l=l[1:]
        l+=p
    k*=(-1)
print(r)
