# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:21:48 2026

@author: Chavosier
"""

"""
F. 清一色
题目描述：
麻将中有条子、饼子、万子三种花色，每种花色都有一到九的牌各四张。
胡牌时玩家手中有 14 张牌；要求 14 张牌中包含一个对子（两张完全相同的牌）和四个面子。
一个面子可以是一个顺子（花色相同的三张连续的牌，例如 345，但不能是 891、912）
或一个刻子（三张完全一样的牌）。
清一色是麻将的一种牌型，指由一种花色组成的一副牌。
现在康已经拿到了 13 张牌，花色都一样，且进入听牌（只要再摸某一张牌就可以和牌）。
你需要告诉他摸到哪几张牌可以和牌。

输入格式：
一行 13 个整数，为现在康手上的牌。

输出格式：
共一行，多个整数，为可以和牌的牌，每个整数用空格隔开。

样例输入：
1 1 1 2 3 4 5 6 7 8 9 9 9
样例输出：
1 2 3 4 5 6 7 8 9

数据范围：
保证数据合法，数据保证进入听牌。
"""

from collections import Counter

a = list(map(int, input().split()))
cnt = Counter(a)

def can_hu(c):
    """
    判断牌型 c（长度为14的Counter或数组）是否可以胡牌。
    胡牌条件：一个对子 + 四个面子（顺子或刻子）
    """
    # 找到第一个数量大于0的牌
    for i in range(1, 10):
        if c[i] > 0:
            break
    else:
        return True  # 所有牌都为0，说明已经分完了

    # 尝试作为刻子
    if c[i] >= 3:
        c[i] -= 3
        if can_hu(c):
            c[i] += 3
            return True
        c[i] += 3

    # 尝试作为顺子（需要 i, i+1, i+2 都存在）
    if i <= 7 and c[i + 1] > 0 and c[i + 2] > 0:
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        if can_hu(c):
            c[i] += 1
            c[i + 1] += 1
            c[i + 2] += 1
            return True
        c[i] += 1
        c[i + 1] += 1
        c[i + 2] += 1

    return False

res = []
for t in range(1, 10):
    if cnt[t] >= 4:
        continue  # 该牌已经有4张，不能再摸
    c = Counter(cnt)
    c[t] += 1
    # 枚举对子
    ok = False
    for pair in range(1, 10):
        if c[pair] >= 2:
            c[pair] -= 2
            if can_hu(c):
                ok = True
                c[pair] += 2
                break
            c[pair] += 2
    if ok:
        res.append(t)

print(' '.join(map(str, res)))