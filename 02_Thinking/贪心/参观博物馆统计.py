# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 02:32:19 2026

@author: Chavosier
"""

'''
题目描述
给出某博物馆一天每位游客的进馆和出馆时间，统计该馆在某指定人数下的超时时间。
每个人进馆出馆时间用一个长度为 11 的字符串表示，如 "08:05-08:45" 表示进馆时间为 8 点 05 分，出馆时间为 8 点 45 分。
要求统计的是当天场馆超过指定人数的时长。

输入格式
第 1 行，两个整数 n、m，n 表示参观游客人数，m 为指定人数。
第 2~n+1 行，每行一个字符串，表示该游客的进馆出馆时间。

输出格式
一个整数，表示当天场馆超过指定人数的时长，单位：分钟。

样例
输入数据 1
6 3
08:05-08:45
08:15-08:50
08:08-08:55
08:10-08:35
08:20-08:42
08:18-08:38
输出数据 1
27
'''

n, m = map(int, input().split())
data = []
for i in range(n):
    tt = input()
    a = 60 * int(tt[0:2]) + int(tt[3:5])
    b = 60 * int(tt[6:8]) + int(tt[9:11])
    data.append([a, 1])
    data.append([b, 2])

data.sort(key=lambda x: x[0])
s = 0
time = 0
flag = False
for i in range(2 * n):
    if data[i][1] == 1:
        s += 1
        if s > m and not flag:
            l = data[i][0]
            flag = True
    else:
        s -= 1
        if s <= m and flag:
            time += data[i][0] - l
            flag = False
print(time)