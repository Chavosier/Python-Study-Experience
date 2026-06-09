'''
Description
一个n * m的方格图，一些格子被涂成了黑色，在方格图中被标为1，白色格子标为0。问有多少个四连通的黑色格子连通块。四连通的黑色格子连通块指的是一片由黑色格子组成的区域，其中的每个黑色格子能通过四连通的走法（上下左右），只走黑色格子，到达该联通块中的其它黑色格子。

Format
Input
第1行两个整数n,m(1<=n,m<=100)，表示一个n * m的方格图。 接下来n行，每行m个整数，分别为0或1，表示这个格子是黑色还是白色。

Output
一行一个整数ans，表示图中有ans个黑色格子连通块。

Samples
输入数据 1
3 3
1 1 1
0 1 0
1 0 1
输出数据 1
3
Limitation
1s, 1024KiB for each test case.
'''
n,m=map(int,input().split())
g=[]
dir=[[-1,0],[1,0],[0,1],[0,-1]]
for i in range(n):
    t=list(map(int,input().split()))
    g.append(t)

def bfs(x0,y0):
    que=[0]*(n*m+1)
    que[0]=[x0,y0]
    g[x0][y0]=-1
    head=0;tail=1
    while head<tail:
        x0,y0=que[head][0],que[head][1]
        head+=1
        for k in range(4):
            x1=x0+dir[k][0]
            y1=y0+dir[k][1]
            if 0<=x1<n and 0<=y1<m and g[x1][y1]==1:
                g[x1][y1]=-1
                que[tail]=[x1,y1]
                tail+=1


num=0
for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            num+=1
            bfs(i,j)
print(num)