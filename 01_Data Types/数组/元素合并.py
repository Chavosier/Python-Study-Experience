# Description
# 基于数组实现数据合并功能。已知一个降序排列的非负整数数列A：a1，a2，a3，a4，a5，以及一个降序排列的非负整数数列B：b1，b2，b3，b4，b5，b6，b7，将两个数列合并形成一个新的有序数列C，使新数列仍按降序排列。

# Format
# Input
# 输入两行，分别是A数组中的元素和B数组中的元素，元素间用空格隔开

# Output
# 输出一行，为合并后的数组元素，元素间用空格隔开

# 此代码
a=list(map(int,input().split()))
b=list(map(int,input().split()))
lena=len(a)
lenb=len(b)
i=0; j=0
c=[0]*(lena+lenb)
for k in range(lena+lenb):
    if i>=lena or (j<lenb and a[i]<=b[j]):
        #a[i]<=b[j]为主要内容，i>=lena or (j<lenb and 是调整
        c[k]=b[j]
        j+=1
    else:
        c[k]=a[i]
        i+=1
for i in range(0,lena+lenb):
    # if c[i]!=c[i-1]:
    #     print(c[i],end=' ')
    print(c[i], end=' ')