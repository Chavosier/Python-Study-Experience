from random import randint

Maxn = 3      # 最大层数
Maxm = 10     # 最大节点数
Data = [0] * (Maxn + Maxm)          # 节点数据（key）
Next = [[-1] for i in range(Maxn + Maxm)]  # Next[i][lev] = 第lev层下一个节点索引
Lev = [0] * (Maxm)                   # 每个节点的实际层数（0-based）
head = 0                             # 头节点索引
node_cnt = 0                         # 已用节点数（不含head）


def Print(lev):
    """打印第lev层的链表。"""
    print('lev=%d:' % lev, end=' ')
    p = Next[head][lev]
    while p != -1:
        print(Data[p], end=',')
        p = Next[p][lev]
    print()


def Print_all():
    """打印所有层。"""
    print('--- 跳表结构 ---')
    for i in range(Maxn):
        Print(i)
    print('Data:', Data[:node_cnt + 1])
    print('Lev: ', Lev[:node_cnt + 1])
    print('----------------')


def Create():
    """创建初始有序数据（第0层）。"""
    global node_cnt
    # 初始化head
    for i in range(Maxn + Maxm):
        Next[i] = [-1] * Maxn

    # 创建第0层基础数据
    node_cnt = 1
    Data[node_cnt] = randint(1, 3)
    Next[head][0] = node_cnt

    for i in range(node_cnt + 1, Maxm):
        Data[i] = Data[i - 1] + randint(1, 3)
        Next[i - 1][0] = i
        node_cnt = i

    # 第0层最后一个节点指向-1
    Next[node_cnt][0] = -1

    print('第0层（基础数据）:')
    Print(0)

    # 逐层建立索引
    for lev in range(1, Maxn):
        p = Next[head][lev - 1]   # 从上一层第一个节点开始
        q = -1                     # 上一层的前一个被选中节点
        while p != -1:
            t = randint(0, 1)     # 50%概率晋升
            if t == 1:
                # p节点晋升到第lev层
                Lev[p] = lev
                if q == -1:
                    Next[head][lev] = p   # 头节点指向第一个晋升节点
                else:
                    Next[q][lev] = p       # 上一层晋升节点指向当前
                q = p
            p = Next[p][lev - 1]   # 继续遍历上一层

        # 最后一个晋升节点指向-1
        if q != -1:
            Next[q][lev] = -1

        Print(lev)


def search(key):
    """查找key，返回索引；不存在返回-1。"""
    # 从最高层开始往下找
    lev = Maxn - 1
    while lev >= 0 and Next[head][lev] == -1:
        lev -= 1

    p = head
    while lev >= 0:
        # 在当前层向右走，直到下一个节点的key >= target
        while Next[p][lev] != -1 and Data[Next[p][lev]] < key:
            p = Next[p][lev]
        lev -= 1

    # 现在p是第0层中key的前驱
    target = Next[p][0]
    if target != -1 and Data[target] == key:
        return target
    return -1


def insert(key):
    """插入key（value暂用key本身）。"""
    global node_cnt

    # 找到每层的前驱节点
    update = [-1] * Maxn
    lev = Maxn - 1
    while lev >= 0 and Next[head][lev] == -1:
        lev -= 1

    p = head
    cur_lev = lev
    while cur_lev >= 0:
        while Next[p][cur_lev] != -1 and Data[Next[p][cur_lev]] < key:
            p = Next[p][cur_lev]
        update[cur_lev] = p
        cur_lev -= 1

    # 检查是否已存在
    target = Next[p][0]
    if target != -1 and Data[target] == key:
        print('key %d 已存在' % key)
        return

    # 创建新节点
    node_cnt += 1
    Data[node_cnt] = key

    # 随机决定层数（从第0层开始，逐层晋升）
    new_lev = 0
    while new_lev < Maxn - 1 and randint(0, 1) == 1:
        new_lev += 1
    Lev[node_cnt] = new_lev

    # 在各层插入
    for i in range(new_lev + 1):
        Next[node_cnt][i] = Next[update[i]][i]
        Next[update[i]][i] = node_cnt


def remove(key):
    """删除key，成功返回True，失败返回False。"""
    # 找到每层前驱
    update = [-1] * Maxn
    lev = Maxn - 1
    while lev >= 0 and Next[head][lev] == -1:
        lev -= 1

    p = head
    cur_lev = lev
    while cur_lev >= 0:
        while Next[p][cur_lev] != -1 and Data[Next[p][cur_lev]] < key:
            p = Next[p][cur_lev]
        update[cur_lev] = p
        cur_lev -= 1

    # 定位目标
    target = Next[p][0]
    if target == -1 or Data[target] != key:
        print('key %d 不存在' % key)
        return False

    target_lev = Lev[target]

    # 从各层删除
    for i in range(target_lev + 1):
        Next[update[i]][i] = Next[target][i]

    # 清理target的next（可选）
    for i in range(target_lev + 1):
        Next[target][i] = -1

    print('删除 %d 成功' % key)
    return True


# ==================== 主程序 ====================
print('=== 创建跳表 ===')
Create()

print('\n=== 查找测试 ===')
print('search(5) =', search(5))
print('search(100) =', search(100))

print('\n=== 插入测试 ===')
insert(50)
insert(60)
Print_all()

print('\n=== 删除测试 ===')
remove(50)
Print_all()
