'''
说明
读入一个算术表达式，检查其中的圆括号是否配对，给出适当信息。
（1）若匹配成功，则输出"Yes!"

（2）若匹配失败，则输出"No!"

输入格式
一行字符
'输出格式
输出圆括号匹配结果
输入数据 1
3*(4-5)+9/2
输出数据 1
Yes!'''
l=input()
sta=[]
top=-1
f=True
for i in l:
    if i=='(':
        sta.append('bite me!')
        top+=1
    elif i==')':
        if top!=-1:
            sta.pop()
            top-=1
        else:
            f=False
            break
if top==-1 and f:
    print('Yes!')
else:
    print('No!')