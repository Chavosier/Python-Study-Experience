'''
Description
对于完全二叉树而言，从二叉树的根节点开始，按从上而下、自左往右的顺序对n个节点进行编号，根节点的编号为0，最后一个节点的编号为n-1。用数组来表示则非常方便，占用了数组中连续的空间。

对于普通二叉树而言，若我们将缺失节点补全，补全后同样可将其看成是一棵完全二叉树。具体如下图所示：

img

Format
Input
输入若干行，每行两个数据，对应为补全后的完全二叉树数组的下标、数组的存储内容

Output
输出叶节点的个数及树的高度

Samples
输入数据 1
0 A
2 B
6 C
输出数据 1
1 3
'''
import sys,math
binary_tree=[0]*1010
n=0
for line in sys.stdin.readlines():
    t=list(line.split())
    t[0]=int(t[0])
    n=max(n,t[0])
    binary_tree[t[0]]=t[1]
n+=1
num=0
k=int(math.log2(n)+0.005)+1
for i in range(0,n):
    if binary_tree[i]!=0 and binary_tree[i*2+1]==0 and binary_tree[i*2+2]==0:
        num+=1
print(num,k)