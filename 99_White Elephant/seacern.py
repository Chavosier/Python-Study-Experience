import seaborn as sns
import matplotlib.pyplot as plt

# 创建一些示例数据
data = {
    "x": [1, 2, 3, 4, 5],
    "y": [5, 4, 3, 2, 1]
}

# 使用 Seaborn 绘制散点图
sns.scatterplot(x="x", y="y", data=data)

# 添加标题和标签
plt.title("图形")
plt.xlabel("X")
plt.ylabel("Y")

# 显示图形
plt.show()