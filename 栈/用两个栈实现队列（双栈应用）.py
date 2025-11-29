'''
Description
请你用两个栈来模拟实现一个队列的操作：

使用两个大小为n的栈来完成在队尾部入整数(push)和在队首删除整数(pop)的功能。 队列中的元素均为int类型。

为确保操作的合法性，应注意下列事项:

（1）保证pop操作时栈中有元素，若没有元素则给出错误信息："ERR Empty!"，并结束后续操作。

（2）队尾插入整数(push)，若栈已装入n个元素，则给出错误信息："ERR Full!"，并结束后续操作。

Format
Input
第一行输入一个整数n，表示栈的大小，如n=4

第二行输入栈的相关操作：

4

push,1,push,3,pop,push,2,pop,pop

Output
1,3,2

Samples
输入数据 1
4
push,1,push,3,pop,push,2,pop,pop
输出数据 1
1,3,2
'''

n=int(input())
l=list(input().split(','));len=len(l)
i=0
sta1=['']*n;top1=-1
sta2=['']*n;top2=-1
re=''
while i<len:
    if l[i]=='push':
        if top1==n-1:
            re+="ERR Full!,"
            break
        i+=1
        top1+=1;sta1[top1]=l[i]
    elif l[i]=='pop':
        if top1==-1:
            re+="ERR Empty!,"
            break
        while top1!=-1:
            top2+=1
            sta2[top2]=sta1[top1]
            top1-=1
        re+=sta2[top2]+','
        top2-=1
        while top2!=-1:
            top1+=1
            sta1[top1]=sta2[top2]
            top2-=1
    i+=1

print(re[:-1])
