# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:28:21 2026

@author: Chavosier
"""
# a=list(map(int,input().split()))
a=[84,-37,62,40,-10,95,24]
s=115

n = len(a)
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + a[i] # 用前缀和处理各组求和 
    # [0, 84, 47, 109, 149, 139, 234, 258]
p = [-1] * (n + 1) # p中存储可能作为 best start 的数据索引, p中索引所代表的数据单增
head = 0; tail = 0
minlen = n + 1; beststart = -1
for k in range(n + 1):
    while head < tail and prefix[k] - prefix[p[head]] >= s: # 用head遍历，尝试缩短数据组得到更短的结果
        left = p[head]
        head = head + 1
        if k - left < minlen: # 检查是否最优
            minlen = k - left
            beststart = left
    # while head < tail and prefix[k] <= prefix[p[tail - 1]]:
    #     tail = tail - 1
    #     # 在p中处理可能的单减反例，保证p单增
    #     # -37和-10 一定不是beststart
    #     # 保证单增有利于直接不考虑这些数据
    p[tail] = k
    tail = tail + 1
    
end=beststart+minlen
print(str(beststart)+' '+str(end))
print(a[beststart:end])
'''
"p中存储可能作为 best start 的数据索引"
"p中索引所代表的数据单增"
第一个 while 旁边
"用head遍历，去除一些没用的数据"
第二个 while 旁边
"对于此k来说，处理可能的反例"
"因为 [109, 149, 139] 中 149 不是 best start"
底部计算
 prefix = [0, 84, 47, 109, 149, 139, 234, 258]
'''