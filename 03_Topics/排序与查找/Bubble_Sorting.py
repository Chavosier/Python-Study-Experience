'''
Description
读入若干个数，使用冒泡排序算法将它们按照从小到大的顺序存储，输出排序后的结果，以及所需的遍数、比较次数和交换次数。（本题适合新手学习，是不加优化的冒泡哦！）

Format
Input
第一行n，n 个元素

第二行n个整数（不会超过1000个）；

Output
第一行为排序后的结果，各个数之间以空格分隔；

第二行为三个整数，分别表示完成冒泡排序所需的遍数、比较次数和交换次数。

Samples
输入数据 1
10
65 33 58 79 93 45 68 82 79 12
输出数据 1
12 33 45 58 65 68 79 79 82 93
9 45 20
'''
n=int(input())
l=input().split()
def Print(l):
    for i in range(len(l)-1):
        print(l[i],end=' ')
    print(l[-1])
q,w,e=0,0,0
for i in range(1,n):
    q+=1
    for j in range(0,n-i):
        w+=1
        if l[j]>l[j+1]:
            e+=1
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
Print(l)
print(str(q)+' '+str(w)+' '+str(e))
