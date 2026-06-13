# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:44:29 2026

@author: Chavosier & Kimi
"""

'''
C. 消息队列（取）

Description
给定一个字符串S1,S2,...,Sn，按如下规则加密：
取第一个字符S1，将第二个字符S2放到字符串末尾Sn后面，得到字符串S3...SnS2...
然后取S3，将S4放到末尾S2后面...
直到最后一个字符Sn被取出，这些字符按取出顺序形成一个新的字符串，称为密文。
请编写一个程序输出密文。

Format
Input
一行字符串，长度不超过100
Output
输出该字符串的密文

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
