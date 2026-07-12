# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 02:29:44 2026

@author: Chavosier
"""

'''
题目描述
有 n 个活动，每个活动需要使用同一资源，且同一时间内只能有一个活动使用该资源。
第 i 个活动有起始时间 s_i 和结束时间 f_i（s_i < f_i）。
若区间 [s_i, f_i) 与 [s_j, f_j) 不重叠（即 f_i ≤ s_j 或 f_j ≤ s_i），则称活动 i 与活动 j 兼容。
选出由互相兼容的活动组成的最大集合。

输入格式
第一行一个整数 n。
接下来 n 行，每行两个整数 s_i 和 f_i。

输出格式
输出最多能安排的兼容活动数量。

样例
输入数据 1
4
1 3
4 6
2 5
1 7
输出数据 1
2
'''

n = int(input())
data = []
for i in range(n):
    t = list(map(int, input().split()))
    data.append(t)

data.sort(key=lambda x: x[1])
r = data[0][1]
s = 1
for i in range(1, n):
    l = data[i][0]
    if l >= r:
        r = data[i][1]
        s += 1
print(s)