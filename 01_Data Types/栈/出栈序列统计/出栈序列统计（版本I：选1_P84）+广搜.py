n,m=map(int,input().split())
ans=[0]*n;tot=-1
sta=[0]*n;top=-1
num=0
def dfs(ans,sta,tot,top,i):#ans,sta本来可以不加，但加上调试方便
    global num
    if tot>=n-1:
        num+=1
        for i in range(n-1):
            print(ans[i],end=' ')
        print(ans[n-1])
        return
    if top>=0:#出栈
        tot+=1
        ans[tot]=sta[top]
        sta[top]=0#清零，调试方便
        top-=1
        dfs(ans,sta,tot,top,i)
        top+=1
        sta[top]=ans[tot]
        ans[tot]=0
        tot-=1
    if top<m-1 and i<=n:#入栈
        top+=1
        sta[top]=i
        dfs(ans,sta,tot,top,i+1)
        sta[top]=0
        top-=1
dfs(ans,sta,tot,top,1)
print(num)

# n, m = map(int, input().split())
# ans = [0] * n
# sta = [0] * n

# def dfs(ans, sta, top, tot, i, num):
#     if tot >= n - 1:  # 如果已经生成了一个完整的出栈序列
#         num += 1
#         print(" ".join(map(str, ans)))
#         return num

#     # 出栈操作
#     if top >= 0:
#         ans[tot + 1] = sta[top]  # 将栈顶元素加入出栈序列
#         num = dfs(ans, sta, top - 1, tot + 1, i, num)  # 递归处理
#         # 回溯时无需清零，直接调整指针即可

#     # 入栈操作
#     if tot < m - 1 and i <= n:
#         sta[top + 1] = i  # 将当前数字入栈
#         num = dfs(ans, sta, top + 1, tot, i + 1, num)  # 递归处理
#         # 回溯时无需清零，直接调整指针即可

#     return num

# # 初始调用
# num = dfs(ans, sta, -1, -1, 1, 0)
# print(num)