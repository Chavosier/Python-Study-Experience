# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:13:15 2026

@author: Chavosier
"""

import random
import math
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # Windows 黑体
plt.rcParams['axes.unicode_minus'] = False #解决负号显示问题

# ====================== 模拟参数 ======================
N0 = 10000       # 初始原子数
lam = 0.1        # 衰变常数 λ
dt = 0.01        # 时间步长
total_time = 30  # 总模拟时间

prob_decay = lam * dt  # 每一步每个原子的衰变概率

# ====================== 蒙特卡洛模拟 ======================
N_remaining = [N0]
times = [0]

current_N = N0
t = 0

while t < total_time and current_N > 0:
    decayed = 0
    # 对每个存活原子，随机判断是否衰变
    for _ in range(current_N):
        if random.random() < prob_decay:
            decayed += 1

    current_N -= decayed
    t += dt

    N_remaining.append(current_N)
    times.append(t)

# ====================== 找实测半衰期 ======================
half_N = N0 / 2
t_half_measured = None

for i in range(len(N_remaining)):
    if N_remaining[i] <= half_N:
        t_half_measured = times[i]
        break

# ====================== 理论半衰期 ======================
t_half_theory = math.log(2) / lam

# ====================== 输出结果 ======================
print(f"理论半衰期 T1/2 = ln2/λ = {t_half_theory:.4f}")
print(f"模拟实测半衰期   = {t_half_measured:.4f}")
print(f"相对误差 = {abs(t_half_measured - t_half_theory)/t_half_theory:.2%}")

# ====================== 绘图 ======================
plt.figure(figsize=(10,5))
plt.plot(times, N_remaining, label='模拟原子数 N(t)')
plt.axhline(y=half_N, color='r', linestyle='--', label='N0/2')
plt.axvline(x=t_half_theory, color='g', linestyle='-.', label='理论半衰期')
plt.xlabel('时间 t')
plt.ylabel('剩余原子数')
plt.title('蒙特卡洛模拟放射性衰变 & 半衰期验证')
plt.grid(True)
plt.legend()
plt.show()