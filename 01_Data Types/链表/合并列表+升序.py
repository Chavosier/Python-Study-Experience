'''
Description
链表指的是将需要处理的数据对象以节点的形式，通过指针串联在一起的一种数据结构。链表中的每个节点一般由数据区域和指针区域两部分构成，其中数据区域用于保存实际需要处理的数据元素，指针区域用来保存该节点相邻节点的存储地址。

已知列表data中存储了两个升序链表，现要将这两个链表按升序进行合并。输出升序排序后链表中各个节点的数据信息。

Format
Input
第1行，n个数据和两个链表的头指针heada、headb。

第2~n+1行，每行为两个数x和y。x表示节点数据区域的值，y表示节点指针区域的值。

Output
对两个链表按升序处理，输出合并后链表中各个节点的数据信息。
'''
'''
12 5 9
9 11
15 8
4 7
2 6
25 -1
3 2
8 10
6 0
23 -1
1 3
17 4
13 1

'''

def Print(l, head):
    # 遍历链表并输出每个节点的数据和指针
    o = head
    while o != -1:
        print(l[o][0], end=' ')
        print(l[o][1])
        o = l[o][1]

n, heada, headb = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
# 添加两个虚拟头结点，方便合并操作
data.append(['@1', heada])
dummya = len(data) - 1
data.append(['@2', headb])
dummyb = len(data) - 1

pa = heada;pb = headb
head = heada;q = dummya
# 选择较小的头结点作为合并后链表的头
if data[heada][0] > data[headb][0]:
    head = headb
    q = dummyb

# 合并两个升序链表

#for _ in range(len(data) - 2):
while pa != -1 or pb != -1:

    #if (data[pa][0]<=data[pb][0] and pa!=-1) or pb==-1:
#在执行该语句时，pa=-1时会跳出，但pa=-1时，data[pa][0]<=data[pb][0] 会报错，
# 我希望即使会报错，也能继续执行下面的else语句
    if (pa != -1 and (pb == -1 or data[pa][0] <= data[pb][0])):
        t = data[pa][1]      # 保存下一个节点索引
        data[q][1] = pa      # 插入数据
        q = pa               # 更新pa(pb)的前继q
        pa = t               # 移动链表a指针
    else:
        t = data[pb][1]
        data[q][1] = pb
        q = pb
        pb = t
Print(data, head)
