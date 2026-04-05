'''
说明
小明做到一道有趣的数学题，题目是这样的：将1到9这九个数字分成三个三位数，不能有重复，三个数字之间比例满足1:2:3，求所有3位数组合。编写python程序，显示所有满足条件的组合。

数据格式
输入
无

输出
输出符合条件的组合，一行一个组合

Samples
输入数据 1

输出数据 1
192 384 576
219 438 657
········· 
'''
for i in range(102,333):
    f1,f2,f3,f0=True,True,True,True
    Ha=[0]*11
    ii=2*i
    iii=3*i
    for j in str(i):
        Ha[int(j)]+=1
        if Ha[int(j)]==2:
            f1=False
    for j in str(ii):
        Ha[int(j)]+=1
        if Ha[int(j)]==2:
            f2=False
    for j in str(iii):
        Ha[int(j)]+=1
        if Ha[int(j)]==2:
            f3=False
    for j in Ha[1:10]:
        if j==0:
            f0=False
    if f1 and f2 and f3 and f0:
        print(str(i)+' '+str(ii)+" "+str(iii))