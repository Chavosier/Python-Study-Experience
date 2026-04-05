'''
Description
冒泡的优化算法,是指当数据已经有序时就停止加工。读入若干个数，使用冒泡排序优化算法将它们按照从大到小的顺序存储，求出加了优化后的冒泡排序所需的遍数。

提示：本题要求练习的是从后往前的冒泡。

Format
Input
第一行n，n 个元素

第二行n个整数（不会超过1000个）；

Output
一个整数，表示加了优化后的冒泡排序所需的遍数。

Samples
输入数据 1
8
89 96 85 84 88 82 78 68
输出数据 1
2
'''
n=int(input())
l=list(map(int, input().split()))

count = 0 # 遍数
n_len = n
while n_len>0:
    swapped = False 
    for i in range(n_len - 1, 0, -1):
        if l[i - 1] < l[i]:  
            l[i - 1], l[i] = l[i], l[i - 1]
            swapped = True
    count += 1   
    if not swapped: 
        break
    n_len -= 1

print(count)
