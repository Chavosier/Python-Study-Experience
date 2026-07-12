# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 02:34:27 2026

@author: Chavosier
"""

'''
题目描述
某群以投票方式选出最受欢迎展品，每张选票有一个展品编号，得票超过总票数一半的展品将获选。
现小明已收集全部选票中的部分（已排序），小明又收到部分选票（未排序）。
需要找出最受欢迎展品的编号。

输入格式
第一行为小明已收集选票，每个展品编号以空格分隔，且已经排序。
第二行为小明收集选票后收到的未排序选票。

输出格式
输出最受欢迎展品的编号，若不存在，则输出 -1。

样例
输入数据 1
AS2D4 D2S05 H50T1 H50T1 H50T1 H50T1 H50T1 H50T1 H50T1 JA303 JA303 K1T03 K1T03 KG061 WA102 WA303
VIP88 H50T1 H50T1 H50T1 H50T1 ES351 H50T1 H50T1 WA303 H50T1 H50T1 H50T1 H50T1 K1T03 KG061
输出数据 1
H50T1
'''

a = list(input().split())
b = list(input().split())
s = {}
for i in range(len(a)):
    if a[i] not in s:
        s[a[i]] = 1
    else:
        s[a[i]] += 1
    if s[a[i]] > (len(a) + len(b)) / 2:
        print(a[i])
        exit()
for i in range(len(b)):
    if b[i] not in s:
        s[b[i]] = 1
    else:
        s[b[i]] += 1
    if s[b[i]] > (len(a) + len(b)) / 2:
        print(b[i])
        exit()
print(-1)