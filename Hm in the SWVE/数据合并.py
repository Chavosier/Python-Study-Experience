'''
Description
基于数组实现数据合并功能。已知一个降序排列的非负整数数列A：a1，a2，a3，a4，a5，以及一个降序排列的非负整数数列B：b1，b2，b3，b4，b5，b6，b7，将两个数列合并形成一个新的有序数列C，使新数列仍按降序排列。

Format
Input
输入两行，分别是A数组中的元素和B数组中的元素，元素间用空格隔开

Output
输出一行，为合并后的数组元素，元素间用空格隔开

Samples
输入数据 1
9 6 4 2 1
40 30 28 26 3 2 1
输出数据 1
40 30 28 26 9 6 4 3 2 2 1 1 
'''
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
i=0
j=0
ans=''
while i<len(l1) or j<len(l2):
    if i<len(l1) and (j==len(l2) or l1[i]>=l2[j]):
        ans+=str(l1[i])+' '
        i+=1
    else:
        ans+=str(l2[j])+' '
        j+=1
print(ans[:-1])