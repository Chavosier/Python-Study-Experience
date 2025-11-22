'''
说明
用栈模拟10进制数m转换成R进制过程，用栈实现m转换成R进制操作。

输入格式
一行共2两个整数：m, R 表示将一个10进制数m转换成R进制（m>=0, 2<=R<=16）

请你用栈模拟10进制数m转换成R进制过程，用栈实现m转换成R进制操作。

输出格式
将栈中元素全部输出，输出若干行，每行输出两个数据，栈顶指针及栈中元素；

最后一行，输出一个转换后得到的R进制数

样例
输入数据 1
179 8
输出数据 1
2 2
1 6
0 3
263'''
m,R=map(int,input().split())
s0='0123456789ABCDEF'
sta=[]
top=-1
while m>0:
    t=m%R
    sta.append(s0[t])
    top+=1
    m//=R
ans=''
while top!=-1:
    t=sta.pop()
    print(top,t)
    ans+=t
    top-=1
print(ans)