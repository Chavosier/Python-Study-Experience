import random
a=[10,20,31,31,31,40,50,60]
key=random.randint(0,100)
i=0;j=len(a)-1
while i<=j:
    m=(i+j)//2
    if key>a[m]:
        i=m+1
    else:
        j=m-1
print(i)# 大于等于key的第一个元素的位置
print(j-i)