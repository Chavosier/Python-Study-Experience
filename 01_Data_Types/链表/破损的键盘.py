'''
Description
你有一个破损的键盘。键盘上所有的键都可以正常工作，但有时候Home键或者End键会自动按下。
你并不知道键盘存在这一问题，而是专心打稿子，甚至连显示器都没打开。当你打开显示器后，展现在你
面前的是一段悲剧文本。你的任务是在打开显示器之前计算出这段悲剧文本。
Input
输入一行数据，包含不超过100000个字母、下划线、字符"["或者"]"。
其中字符"["表示Home键，"]"表示End键。
This_is_a_[Beiju]_text
 Output
输出一行文本，即屏幕上的悲剧文本。
BeijuThis_is_a_text
输入数据 1
 This_is_a_[Beiju]_text
输出数据 1
 BeijuThis_is_a__text

'''
data='@'+input()
node=[-1 for i in range(len(data))]

dummy=0;tail=0
cur=0#current
#node[i] 表示 字符 data[i] 的下一个字符的索引
for i in range(1,len(data)):
    x=data[i]
    if x=='[':
        cur=dummy
    elif x==']':
        cur=tail
    else:
        node[i]=node[cur]#把cur光标后面的接到i后
        node[cur]=i#把i插入到cur光标位置
        if cur==tail:
            tail=i
        cur=i
p=node[dummy]
while p!=-1:
    print(data[p],end='')
    p=node[p]