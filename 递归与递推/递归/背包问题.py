'''
题目描述
简单的背包问题。设有一个背包，可以放入的重量为s。现有n件物品，重量分别为 w1, w2, …, wn (1≤i≤n) 均为正整数，
从n件物品中挑选若干件，使得放入背包的重量之和正好为s。找到一组解即可（若存在多组，则编号从小到大排列，输出的这组编号按字典顺序排列最小。若无解，则输出 not found）。

输入格式
第一行是物品总件数和背包的载重量，第二行为各物品的重量。

输出格式
各所选物品的序号和重量。

样例
输入数据 1
5 10
1 2 3 4 5
输出数据 1
number:1 weight:1
number:2 weight:2
number:3 weight:3
number:4 weight:4
'''
n,w_s=map(int,input().split())
w=[0]+list(map(int,input().split()))
error='not found'
def bag(w_s,x,n,w):
    # 查找从x到n中，能否找到若干物品，使得它们的重量和为w_s
    if w_s<0:
        return error
    if w_s==0:
        return []
    for i in range(x,n+1):# 相当于变化x的值
        t=bag(w_s-w[i],i+1,n,w)
        # t=bag(w_s-w[i],x+1,n,w)  3 10   1,5,5
        if t!=error:
            return [i]+t
    return error
key=bag(w_s,1,n,w)
if key==error:
    print(error)
else:
    for k in (key):
        print(f'number:{k} weight:{w[k]}')