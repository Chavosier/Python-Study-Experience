'''
Description
伐木工人Mirko需要砍M 米长的木材。对Mirko来说这是很简单的工作，因为他有一个漂亮的新伐木机，可以如野火一般砍伐森林。不过，Mirko只被允许砍伐一排树。

Mirko的伐木机工作流程如下：Mirko设置一个高度参数 H（米），伐木机升起一个巨大的锯片到高度H，并锯掉所有树比H高的部分（当然，树木不高于H米的部分保持不变）。Mirko就得到树木被锯下的部分。例如，如果一排树的高度分别为20,15,10和17，Mirko 把锯片升到15米的高度，切割后树木剩下的高度将是15,15,10 和15，而 Mirko 将从第1棵树得到5米，从第4棵树得到2米，共得到7米木材。

Mirko 非常关注生态保护，所以他不会砍掉过多的木材。这也是他尽可能高地设定伐木机锯片的原因。请帮助 Mirko 找到伐木机锯片的最大的整数高度H，使得他能得到的木材至少为M米。换句话说，如果再升高1米，他将得不到M米木材。

Format
Input
第1行2个整数N和M，N表示树木的数量，M表示需要的木材总长度。 第2行N个整数表示每棵树的高度。

Output
1个整数，表示锯片的最高高度。

Samples
输入数据 1
4 7
20 15 10 17
输出数据 1
15
输入数据 2
5 20
4 42 40 26 46
输出数据 2
36
'''
n,m=map(int,input().split())
l=list(map(int,input().split()))
i=0
while i<n-1:
    k=i;i=n
    for j in range(n-1,k,-1):
        if l[j]>l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
            i=j
# print(l)
l=l+[0]
for i in range(1,n+1):
    key=l[i]
    s=0
    for j in range(n+1):
        ss=l[j]-key
        if ss<=0:
            break
        else:
            s+=ss
    if s>=m:
        break
# print(i)
for v in range(l[i-1],l[i]-1,-1):
    key=v
    s=0
    for j in range(n+1):
        ss=l[j]-key
        if ss<=0:
            break
        else:
            s+=ss
    if s>=m:
        break
print(v)
'''
4 7
20 14 10 17
'''