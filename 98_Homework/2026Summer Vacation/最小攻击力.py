# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:20:43 2026

@author: Chavosier
"""

"""
H. 扫
题目描述：
玩家初始生命值 M，依次挑战 N 个敌人。
第 i 个敌人生命值 Hi，每回合伤害 Di。
每回合玩家先攻击（造成 X 伤害），若敌人生命 ≤ 0 则被击败且不反击；
否则敌人反击，玩家失去 Di 生命。
生命不会回复，击败所有敌人后玩家剩余生命必须 > 0。
求最小的整数攻击力 X。

输入格式：
第一行包含两个正整数 N 和 M。
第二行包含 N 个正整数 H1, H2, ..., Hn。
第三行包含 N 个正整数 D1, D2, ..., Dn。

输出格式：
输出一个整数，表示通关所需的最小攻击力 X。

样例输入：
2 20
10 5
5 10

样例输出：
5

数据范围：
1 ≤ N ≤ 10⁵, 1 ≤ M ≤ 10¹⁴, 1 ≤ Hi, Di ≤ 10⁹
"""

n, M = map(int, input().split())
H = list(map(int, input().split()))
D = list(map(int, input().split()))

def Check(x):
    """检测最小能量 x 是否可以通关"""
    val = M  # 玩家初始能量
    for i in range(n):
        h, d = H[i], D[i]
        # 需要攻击的回合数：ceil(h / x) - 1（最后一击敌人死亡，不反击）
        k = (h - 1) // x
        val -= k * d
        if val <= 0:
            return False
    return True

L = 1
R = int(1e9)
while L < R:
    mid = (L + R) // 2
    if Check(mid):  # 找到可行解，尝试更小
        R = mid
    else:
        L = mid + 1

print(L)