'''
Description
若数组lst中有Maxn个元素，对应索引为0..Maxn-1，用该数组构建栈方法如下：

（1）栈空条件：top=-1

（2）入栈操作：更新栈顶指针位置，然后放置数据：top=top+1; lst[top]=x

（3）栈满处理：当栈顶指针top==Maxn-1时栈满！此时不能再放数据在栈中。

说明：

当执行入栈操作时，若栈已满，则输出"ERR full!"，直接结束后面操作；

当执行出栈操作时，若栈为空，则输出"ERR empty!"，直接结束后面操作；

当对栈进行询问时，若栈非空，则输出栈中最小值,若为空栈，则输入"None!"，后面操作继续执行。

Format
Input
输入数据共两行：

第一行为一个整数n，描述数组的大小；

第二行为一行字符，描述入栈和出栈：

其中字符“I”表示入栈，后面数据表示入栈元素；

字符“O”表示出栈，后面则没有数据。

字符"Q"表示询问，此时输出栈顶元和栈中最小值，若栈为空栈，则输入"None!"

Output
一行，多个数据 （输出的数据若有多个，则用”,“间隔） ERR full!

Samples
输入数据 1
4
I,6,I,7,I,3,I,11,Q,O,Q,O,Q,I,4,I,9,Q,I,17
输出数据 1
3,11,3,3,6,4,ERR full!
'''
'''
5
I,7,I,3,I,2,I,17,O,O,Q,O,Q,O,Q,I,17,Q
'''
n = int(input())
d = list(input().split(','))
top = -1
sta = []
ans=''
f=False
i=0
qq=''
while i != len(d):
    if d[i] == 'I':
        if top==n-1:
            qq='ERR full!'
            f=True
            break
        sta.append(d[i+1])
        top+=1
        i+=1
    elif d[i] == 'O':
        if top==-1:
            qq='ERR empty!'
            f=True
            break
        tt=sta.pop(-1)
        top-=1
        ans+=str(tt)+','
    else:
        if top==-1:
            ans+='None!,'
        else:
            a=top
            min=10**3
            while a!=-1:
                if min>int(sta[a]):
                    min=int(sta[a])
                    t=a
                a-=1
            ans += sta[t] + ','
    i+=1
if not f:
    print(ans[:-1]+qq)
else:
    print(ans+qq)
