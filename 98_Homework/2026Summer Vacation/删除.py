# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:24:43 2026

@author: Chavosier
"""

"""
E. 删除
题目描述：
给定一个长度为 N 的字符串 s，仅包含 R、G、B。
可以删除若干字符，使得剩下的字符串中任意相邻字符不同。
求最少删除数量。

输入格式：
第一行是一个整数 N。
第二行是一个长度为 N 的字符串 s。

输出格式：
一行一个整数，表示最少需要删除的字符数量。

样例输入：
5
RRBRR
样例输出：
2

数据范围：
1 ≤ N ≤ 10⁵
"""

n = int(input())
s1 = input().strip()
num = 0
for i in range(1, n):
    if s1[i] == s1[i - 1]:
        num += 1
print(num)


