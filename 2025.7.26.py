#30．有6个相同的球，分别标有数字1、2、3、4、5、6，从中不放回地随机抽取3次，
# 每次取1个球．记表示前两个球号码的平均数，记表示前三个球号码的平均数，则与差的绝对值不超过的概率是 　　．


# import math
import random
m=100000
k=0
for i in range(m):
    sum3n=0
    sum2n=0
    l=[1, 2, 3, 4, 5, 6]
    for j in range(2):
        n=random.randint(0, len(l)-1)
        sum2n+=l[n]
        sum3n+=l[n]
        del l[n] 
    n=random.randint(0, len(l)-1)
    sum3n+=l[n]
    sum2n/=2
    sum3n/=3
    if abs(sum2n-sum3n)<=0.5:
        k+=1
print(k/m)
print(7/15)                  # Output the probability
