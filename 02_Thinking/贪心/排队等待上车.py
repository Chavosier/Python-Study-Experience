# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 02:35:25 2026

@author: Chavosier
"""

'''
题目描述
某旅游景点游客排队等待上车，游客信息由目的地和登车时间组成。
不同目的地的游客分不同车，同一目的地的游客可同乘一辆车。
每辆车最多乘坐 v 人，每位游客的等待时间都不超过 w 分钟。
游客信息中目的地和登车时间由长度为 7 的字符串表示，如 "A-09:15" 表示游客的目的地为 A，9 点 15 分到达登车点。
若 w 为 10，则该游客将在 9 点 25 分前必须出发去目的地。
编写程序统计 n 位游客最少需要多少辆车。

输入格式
第一行为三个整数 n(1≤n≤1000)、v(4≤v≤30)、w(5≤w≤60)。
接下来 n 行，每行为游客的目的地和登车时间，是长度为 7 的字符串。

输出格式
输出最少需要的车辆数。

样例
输入数据 1
10 5 10
A-08:03
A-08:38
A-08:41
A-08:45
A-08:46
A-08:46
B-08:01
B-08:02
B-08:05
B-08:07
输出数据 1
3
'''

n, v, w = map(int, input().split())
data = []
for i in range(n):
    tt = input()
    a = tt[0]
    b = int(tt[2:4]) * 60 + int(tt[5:])
    data.append([a, b])

data.sort(key=lambda x: x[1])
ans = 0
used = [False] * n # 是否已经坐车走了

for i in range(n):
    if used[i]: # skip
        continue
    used[i] = True
    ty = data[i][0]
    ti = data[i][1]
    vc = 1
    for j in range(i + 1, n):
        if not used[j] and data[j][0] == ty and data[j][1] <= ti + w and vc < v:
            used[j] = True
            vc += 1
    ans += 1

print(ans)