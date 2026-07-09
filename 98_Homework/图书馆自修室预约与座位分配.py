# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:54:36 2026

@author: Chavosier & Kimi
"""
def creat(y, st, ed, n):
    h = []
    t = []
    
    # 存储某时段各座位指示灯信号，0 表示灯绿，1 表示灯黄，2 表示灯红
    d = [0] * (n + 1)
    
    # 数组 t 存储各时段被预约的座位号
    for i in range(ed + 1):
        t.append([])
    
    # 遍历预约单，将座位号填入对应时段
    for p in y:
        for q in range(p[1], p[2]):
            k = p[0]
            t[q].append(k)
    
    # 逐时段生成指示灯信号
    for i in range(st, ed):
        # 上一时段被预约的座位，当前时段默认变绿
        for j in t[i - 1]:
            d[j] = 0
        
        # 当前时段被预约的座位，指示灯变红
        for j in t[i]:
            d[j] = 2
        
        # 下一时段被预约、且当前为绿的座位，指示灯变黄
        for j in t[i + 1]:
            if d[j] == 0:
                d[j] = 1
        
        # 将 1~n 号座位的状态加入信号表（d[0] 不用）
        h.append(d[1:])
    
    return h


def trans(h):
    # 在末尾追加一行全 0，表示关门后所有座位空闲（作为倒序递推边界）
    h.append([0] * n)
    
    # 从倒数第二行倒序遍历到第 0 行
    for i in range(len(h) - 2, -1, -1):
        for j in range(n):
            # 若当前时段座位为绿(0)或黄(1)，表示当前无人占用
            if h[i][j] == 0 or h[i][j] == 1:
                # 加框处（原题错误代码：h[i][j] = h[i - 1][j] + 1）
                # 应修改为：
                h[i][j] = h[i + 1][j] + 1   # 连续空位时段数累加
            else:
                h[i][j] = 0                   # 语句 1：当前时段为红，空位数重置为 0
    
    return h

# 获取当天的预约单数据，存入数组 y
# 获取该静音自修室的开门时间、关门时间以及自修室座位数量，依次存入 st、ed 和 n
# 获取读者输入的到达和离开时间，依次存入 at、pt，代码略
y=[[1, 8, 11],  
   [4, 8, 12],  
   [2, 9, 13], 
   [3, 11, 12],
   [1, 13, 14]]
st,ed=5,20
n=4

at = input("请输入到达时间,如 10:25：")
pt = input("请输入离开时间,如 14:20：")
t1 = int(at[:2])            # 提取到达时间的小时数
t2 = int(pt[:2]) + 1       # 提取离开时间的小时数，+1 转为时段右边界

h = creat(y, st, ed, n)     # 获取自修室指示灯信号表
d = trans(h)                # 将指示灯信号表转化为空位统计表

tot = 0
res = []                    # 数组 res 存储读者各使用时段的座位号
td = t2 - t1                # 计算需要使用的时段总数

flag = True
i = t1 - st                 # 计算相对于开门时间的时段偏移

while i < t2 - st:
    if tot == 0:
        m = 0
        # 查找当前时段连续空位最多的座位（序号小的优先）
        for j in range(1, n):
            if d[i][j] > d[i][m]:
                m = j
        if d[i][m] == 0:    # 若最大连续空位数为 0，则无空位可用
            flag = False
            break
        
        tot = d[i][m]       # 记录该座位可连续使用的时段数
    else:
        res.append(m + 1)   # 记录当前时段分配的座位号（转为 1-based）
        
        if tot >= td:
            d[i][m] -= td   # 该座位连续空位足够覆盖剩余需求
        else:
            d[i][m] -= tot  # 该座位连续空位不足，用完为止
        
        tot -= 1            # 当前座位剩余可用时段数减 1
        td -= 1             # 读者剩余需求时段数减 1
    i += 1                  # 进入下一时段

if flag == False:
    print("座位安排失败！")
else:
    print(t1, "~", t2, "中各时段座位安排：", res)
