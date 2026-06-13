# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 21:49:58 2026

@author: Chavosier & Kimi
"""

'''
I. 栅栏密码（加密）

Description
栅栏密码是一种换位密码，其加密方法是将要加密的明文分成若干组（m个字符一组），然后取每组的第i个字符连接起来形成一组。一般比较常用的是2栏栅栏密码。
例如将"THEREISACIPHER"分成若干组，得到TH,ER,EI,SA,CI,PH,ER，然后取每组的第1个字母得到TEESCPE，取每组的第2个字母得到HRIAIHR，最后连接起来得到"TEESCPEHRIAIHR"。解密时，将密文分成两半TEESCPE和HRIAIHR，再按上下位交错排列得到原文"THEREISACIPHER"。

给定m和明文，使用栅栏密码进行加密，输出密文。

Format
Input
第一行是一个整数m
第二行是待加密的明文
Output
一行，使用栅栏密码加密后的密文。

Samples
3
abcdef
adbecf

Limitation
1s, 1024KiB for each test case.
'''

k=int(input())
ww=['']*k
l=input()
r=''
for i in range(len(l)):
    ww[i%k]+=l[i]
for i in range(k):
    r+=ww[i]
print(r)
