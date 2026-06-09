'''
Description
大数学家高斯小时候偶然间发现一种有趣的自然数集合Blah，对于以a为基的集合Ba定义如下：

（1）a是集合Ba的基，且a是Ba的第一个元素；

（2）如果x在集合Ba中，则2x+1和3x+1也都在集合Ba中；

（3）没有其他元素在集合Ba中了。

现在小高斯想知道如果将集合Ba中元素按照升序排列，第N个元素会是多少？

Format
Input
输入有若干行，每行输入包括两个数字，集合的基a(1<=a<=50))以及所求元素序号n(1<=n<=1000000)

Output
对于每个输入，输出集合Ba的第n个元素值
'''

def ans(s):
    a = int(s[0])
    n = int(s[1])

    # 初始化队列
    que = [0] * n
    que[0] = a
    head = 0
    tail = 1

    queA = [0] * n
    headA = tailA = 0

    queB = [0] * n
    headB = tailB = 0

    while tail < n:
        # 生成新元素并加入队列A和队列B
        if True:
            #if headA == tailA or queA[tailA - 1] != 2 * a + 1:
            queA[tailA] = 2 * a + 1
            tailA += 1
        if True:
            #if headB == tailB or queB[tailB - 1] != 3 * a + 1:
            queB[tailB] = 3 * a + 1
            tailB += 1

        # 去重处理
        if queA[headA] == que[tail - 1]:
            headA += 1
        if queB[headB] == que[tail - 1]:
            headB += 1

        # 比较队列A和队列B的头部，选择较小值加入主队列
        if queA[headA] < queB[headB]:
            que[tail] = queA[headA]
            headA += 1
        else:
            que[tail] = queB[headB]
            headB += 1

        # 更新当前基数
        a = que[tail]
        tail += 1

    return que[n - 1]

# 主循环读取输入
while True:
    try:
        s = input().split()
        result = ans(s)
        print(result)
    except EOFError:
        break