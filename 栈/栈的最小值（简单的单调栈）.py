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
Maxn = int(input())
sta=[None]*Maxn
top=-1
s1=input().split(',')
res=""
flag=False

i=0
while i<len(s1):
    if s1[i]=='I':
        if top<Maxn-1:
            top+=1
            if top==0:
                sta[top]=[int(s1[i+1]),int(s1[i+1])]
            else:
                sta[top]=[int(s1[i+1]),min(int(s1[i+1]),sta[top-1][1])]
            i+=2
        else:
            res+="ERR full!"
            flag=True
            break
    elif s1[i]=='O':
        if top>=0:
            res+=str(sta[top][0])+","
            top-=1
            i+=1
        else:
            res+="ERR empty!"
            flag=True
            break
    elif s1[i]=='Q':
        if top>=0:
            res+=str(sta[top][1])+","
        else:
            res+="None!,"
        i+=1
if not flag:
    print(res[:-1])
else:
    print(res)