
# 计算水桶容积的函数
def calculate_volume(width, height):
    pi = 3.14
    base_area = width * height
    max_dimension = max(width, height)
    return base_area * max_dimension / (4 * pi)

# 主函数
def max_bucket_volume(heights):
    heights.append(0)  # 添加一个哨兵，确保栈中元素全部弹出
    n = len(heights)
    stack = []  # 单调递增栈
    max_volume = 0

    for i in range(n):
        # 当当前高度小于栈顶高度时，计算容积
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]  # 弹出栈顶高度
            if not stack:
                break  # 如果栈为空，跳出循环
            width = i - stack[-1] - 1  # 计算宽度
            volume = calculate_volume(width, height)
            max_volume = max(max_volume, volume)
        stack.append(i)  # 当前索引入栈

    return max_volume

# 输入处理
heights = list(map(int, input().split()))
result = max_bucket_volume(heights)
print(f"{result:.1f}")