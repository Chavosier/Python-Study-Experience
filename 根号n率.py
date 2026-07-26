# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ====================== 物理参数 ======================
lam = 0.1
dt = 0.01
total_time = 30
prob_decay = lam * dt
t_half_theory = np.log(2) / lam
max_steps = int(total_time / dt)

# ====================== 批量向量化模拟（极速） ======================
def sim_batch(N0, n_trials):
    """
    一次性并行模拟 n_trials 个衰变样本，返回所有样本的半衰期绝对误差
    """
    half = N0 / 2.0
    # 初始化：所有样本初始原子数都是 N0
    remaining = np.full(n_trials, N0, dtype=np.int64)
    # 记录每个样本的半衰期，初始为 nan
    t_half = np.full(n_trials, np.nan)
    
    t_prev = 0.0
    remaining_prev = remaining.copy()
    
    for step in range(max_steps):
        # 所有样本一步衰变，二项分布批量抽样
        decayed = np.random.binomial(remaining, prob_decay)
        remaining = remaining - decayed
        t_current = t_prev + dt
        
        # 找到刚跨过半衰期的样本（上一步>half，这一步<=half）
        mask = (remaining_prev > half) & (remaining <= half)
        if np.any(mask):
            # 线性插值计算精确半衰期，消除 dt 离散误差
            n1 = remaining_prev[mask]
            n2 = remaining[mask]
            ratio = (n1 - half) / (n1 - n2)
            t_half[mask] = t_prev + ratio * dt
        
        # 所有样本都已测到半衰期，提前退出
        if not np.any(np.isnan(t_half)):
            break
        
        # 更新上一步状态
        remaining_prev = remaining.copy()
        t_prev = t_current
    
    # 处理极少数没衰变完的样本（理论上不会出现）
    t_half[np.isnan(t_half)] = total_time
    
    return np.abs(t_half - t_half_theory)

# ====================== 主程序 ======================
# 均匀增长 N0（等差数列）
N0_list = np.arange(1000, 30001, 1000)
n_trials = 3000  # 每组500次试验，平滑度足够且速度极快

mean_err_sq = []
for N0 in N0_list:
    errors = sim_batch(N0, n_trials)
    avg_sq = np.mean(errors ** 2)
    mean_err_sq.append(avg_sq)
    print(f"N0 = {N0:5d} | 均方误差 = {avg_sq:.8f}")

inv_err_sq = 1.0 / np.array(mean_err_sq)

# ====================== 绘图 ======================
plt.figure(figsize=(10, 5))
plt.plot(N0_list, inv_err_sq, 'o-', linewidth=2, markersize=5, label='模拟值 1/σ²')
plt.xlabel('初始粒子数 N0')
plt.ylabel('1 / 均方误差')
plt.title('1/误差² 与 N0 的线性关系（插值平滑 + 批量加速）')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()