'''
说明
有 n 个猴子，按顺时针方向围成一个圈选大王。从第1号开始报数 1，2，…… ，数到 m 号时该猴子退出到圈外，如此报数直到圈内只剩下一个猴子时，此猴子便是大王。由键盘输入 n， m ，打印出猴子大王序号。
说明：本题要求使用队列来实现。

输入格式
一行2个整数，n，m（n、m均小于10000）
输出格式
输出共两行：

第一行，依次输出猴子的出队序列；

第二行，一个整数，输出猴王的编号；

输入数据 1

10 3
输出数据 1

3 6 9 2 7 1 8 5 10
4
'''
n,m=map(int,input().split())
q=list(range(1,n+1))+[0]
tail=len(q)-1
head=0
while (tail-head+len(q))%len(q)!=1:
    for i in range(m-1):
        k=q[head]
        head=(head+1)%len(q)
        q[tail]=k
        tail=(tail+1)%len(q)
    k=q[head]
    head=(head+1)%len(q)
    print(k,end=' ')
print()
print(q[head])