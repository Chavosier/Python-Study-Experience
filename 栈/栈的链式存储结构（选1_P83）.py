'''
Description
用单链表存储栈中元素，指针top指向栈顶元素所在的位置，具体如下图所示：

img

用单链表构建栈方法如下：

（1）栈空条件：top==-1

（2）入栈操作：分配新数据空间，放置数据，然后更新栈顶指针位置：

sta.append(x); sta[top][1]=len(sta)-1; top=len(sta)-1

（3）出栈操作：删除栈顶元素，然后更新栈顶指针位置： top=sta[top][1]

（4）栈满处理：链式栈可以临时分配不连续的数据空间,通常不再探讨栈满条件

说明：

当执行出栈操作时，若栈为空，则输出"ERR empty!",后续操作将不再执行。

Format
Input
输入一行字符，描述入栈和出栈：

其中字符“I”表示入栈，后面数据表示入栈元素； 字符“O”表示出栈，后面则没有数据。 如：I,3,I,5,O,I,7,I,19,O,O,O,O

Output
出栈时，输出数据值及存储指针（用空格间隔），如：5 1

空栈时执行出栈操作，则输"ERR empty!"，后续操作将不再执行。

Samples
输入数据 1
I,3,I,5,O,I,7,I,19,O,O,O,O
输出数据 1
5 1
19 3
7 2
3 0
ERR empty!
'''
s=input().split(',')
data=[];head=-1;tail=-1
i=0
while i<len(s):
    if  s[i]=='I':
        i+=1
        x=s[i]
        if head==-1:
            data.append([x,-1])
            head=0
            tail=0
        else:
            data.append([x,-1])
            data[tail][1]=len(data)-1
            tail=len(data)-1
    elif s[i]=='O':
        if tail==-1:
            print("ERR empty!")
            break
        else:
            print(data[tail][0],tail)
            p=head;q=head
            while data[q][1]!=-1:
                p=q
                q=data[q][1]
            if p==q:
                head=-1
                tail=-1
            else:
                data[p][1]=-1
                tail=p
    i+=1

# s=input().split(',')
# stack=[];top=-1
# i=0
# while i<len(s):
#     if s[i]=='I':
#         i+=1
#         x=s[i]
#         top+=1
#         stack.append([x,top])
#     elif s[i]=='O':
#         if len(stack)==0:
#             print("ERR empty!")
#             break
#         else:
#             print(stack[-1][0],stack[-1][1])
#             stack.pop(-1)
#     i+=1