import random
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
matplotlib.rcParams['axes.unicode_minus'] = False    # 正常显示负号
import matplotlib.pyplot as plt

x = [i / 100 for i in range(5, 100, 5)]  # 0.05 到 0.95 步长0.05
y = []
for n in x:
    li = []
    j = 1
    while j <= 10000:  # 次实验
        pop = 100
        l = list(range(1, pop + 1))  # 生成一个列表
        random.shuffle(l)  # 打乱列表顺序
        n_num = round(len(l) * n)
        max_n = max(l[:n_num]) if n_num > 0 else -1

        m = l[-1]
        for i in range(n_num, len(l)):
            if l[i] > max_n:
                m = l[i]
                break

        max_true = max(l)
        if max_true == m:
            li.append(1)
        else:
            li.append(0)
        j += 1

    w = sum(li) / len(li) * 100  # 成功率
    y.append(w)

# 找到最大成功率及对应观察比例
max_rate = max(y)
best_n = x[y.index(max_rate)]
print(f"最大成功率为：{max_rate:.2f}%，对应的观察比例为：{best_n:.2f}")
# 绘制折线图
plt.plot(x, y, marker='o')
plt.xlabel('观察比例')
plt.ylabel('成功率(%)')
plt.title('37%问题成功率随观察比例变化')
plt.grid(True)
plt.show()

