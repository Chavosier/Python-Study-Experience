'''
Description
龙国想对一块矩形（n*m）海域实施填海造陆，该海域内不同位置分布着珊瑚礁，由珊瑚礁围成的闭合区域适合填海造陆，现在龙国请你对该海域进行考察测量，并算出该海域范围由珊瑚礁能围成的所有面积和，即陆地面积。

Format
Input
输入一块矩形区域，0表示海面，1表示存在珊瑚礁。

第1行读入两个整数n，m，表示矩形海域的大小（n行*m列）

接下来读入n行，每行m个整数，表示矩形海域信息（n行*m列）

面积的计算方法是统计海域中由珊瑚礁“1”围成的闭合曲线中，所有海面“0”的数目（即海面“0”组成的图形的上下左右四周均为珊瑚礁“1”）。

Output
输出该海域范围内能够实施填海造陆的总面积。

Samples
输入数据 1
10 10
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 1 0 0 1 0 0
0 0 0 0 0 1 0 0 1 0
0 0 1 0 0 0 1 0 1 0
0 1 0 1 0 1 0 0 1 0
0 1 0 0 1 1 0 1 1 0
0 0 1 0 0 0 0 1 0 0
0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0
输出数据 1
15
Limitation
1s, 1024KiB for each test case.

说明：计算面积时，只计算闭合曲线内海面“0”的数目，珊瑚礁不计算在内，可能存在多个闭合曲线，需计算总面积。'''
# a,n=map(int,input().split())
# que=[0]*n
# que[0]=a;head=0;tail=1
# queA=[0]*n;headA=tailA=0
# queB=[0]
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
            if 0<=x1<n and 0<=y1<m and g[x1][y1]==0:
                g[x1][y1]=-1
                que[tail]=[x1,y1]
                tail+=1
    head=0
    while head<tail:
        x2, y2 = que[head][0], que[head][1]
        if x2 == 0 or x2 == n - 1 or y2 == 0 or y2 == m - 1:
            return 0
        head+=1
    return tail


ans=0
for i in range(n):
    for j in range(m):
        if g[i][j]==0:
            part=bfs(i,j)
            ans+=part
print(ans)
'''
3 5
1 1 1 1 1
1 0 1 0 1
1 1 1 1 1'''