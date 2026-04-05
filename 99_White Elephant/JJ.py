# m,n=map(int,input().split())
# nums=list(map(int,input().split()))
# left = max(nums)  # 最小可能值：数组中的最大值（每段至少包含一个元素）
# right = sum(nums)  # 最大可能值：整个数组的和（即不分段的情况）
#
#     # 定义验证函数，检查是否可以将数组分成不超过n段，每段和不超过mid
# def is_valid(mid):
#     current = 0  # 当前段的和
#     count = 1  # 分段计数（初始已经有1段）
#     for num in nums:
#         if current + num > mid:  # 如果当前段和超过mid
#             count += 1  # 需要新增一段
#             current = num  # 新段从当前元素开始
#             if count > n:  # 如果分段数超过n
#                 return False  # 说明mid太小
#         else:
#             current += num  # 否则继续累加到当前段
#     return True  # 如果成功分成不超过n段，返回True
#
#     # 二分查找主循环
# while left < right:
#     mid = (left + right) // 2  # 取中间值
#     if is_valid(mid):  # 如果mid可行
#         right = mid  # 尝试更小的值
#     else:  # 如果mid不可行
#         left = mid + 1  # 需要更大的值
#
#     # 打印最终结果（left就是最小的最大子段和）
# print(left)

m,n=map(int,input().split())
l=list(map(int,input().split()))
top=max(l)#前限
botten=sum(l)#后限
mid=(top+botten)//2
def f(x):#检查mid在n限度下是否合法
    flag=True
    s=0
    num=1#组数
    for i  in l:
        s+=i
        if s>mid:
            s=i
            num+=1
    if num>n:#所需分的组数比n大，无法让mini值小于mid
        flag=False


    return flag
while top<botten:
    if f(mid):#botten can be more small
        botten=mid
        mid=(botten+top)//2
    else:
        ###top+=1
        if top+1==botten:
            top+=1
        else:#mid should be bigger
            top=mid
        mid=(botten+top)//2
print(top)


