m,n=map(int,input().split())
l=list(map(int,input().split()))

def zuhe(m,n):
    # “”“
    # 生成m个元素的n个组合
    # :param m: 元素总数
    # :param n: 组合个数
    # :return: 返回一个二维数组，包含所有组合


    result = []
    a = []
    b = []  # b=a will made b is the same as always
    b.append(m - n + 1)
    for i in range(n - 1):
        a.append(1)
        b.append(1)
    a.append(m - n + 1)
    result.append(a[:])#advoid result change
    while a != b:
        a[-1] -= 1
        a[-2] += 1
        i = -2
        while -i != n:
            if m - sum(a[:i]) + i + 2 == a[i]:#判断是否可以进位
                a[i - 1] += 1#进位
                a = a[:i] + [1] * (-i - 1) + [m - sum(a[:i]) + i + 1]
            else:
                break
            i -= 1
        result.append(a[:])
    return result
zuhere=zuhe(m,n)
#print(zuhere)
def movedown(x):
    result0=[]
    for i in x:
        re=[]
        s=0
#一个变量设置与使用的缩进位置相同
        for j in i:
            re0=l[s:s+j]
            s+=j
            re.append(re0[:])
        result0.append(re[:])
    return result0
movedresult =movedown(zuhere)
#print(movedresult)
list_summax=[]
for i in movedresult:
    summax=0
    for j in i:
        sum=0
        for k in j:
            sum+=k
        if sum>summax:
            summax=sum
    list_summax.append(summax)
print(min(list_summax))


