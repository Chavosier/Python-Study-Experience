'''
Background
将中缀表达式转换为后缀表达式

Description
Format
Input
.输入中缀表达式

Output
输出后缀表达式

Samples
输入数据 1
3+4*5-8/2
输出数据 1
3 4 5 * + 8 2 / -
输入数据 2
37+24*(5-318)/200
输出数据 2
37 24 5 318 - * 200 / +
Limitation
1s, 1024KiB for each test case.
'''
# by Meurcolt
def Checkcouple(x):
    '''
    检查括号是否匹配
    '''
    flag_checkcouple=True
    sta=[];top=-1
    for i in x:
        if i=='(':
            sta.append('@');top+=1
        elif i==')':
            if top==-1:
                flag_checkcouple=False
                break
            else:
                sta.pop();top-=1
    if top==-1 and flag_checkcouple:
        return True
    else:
        return False

def drasplit(y,dra):
    '''
    按照运算符分割表达式
    输出两个列表：分割后的表达式列表和运算符列表
    '''
    y_splited=[];y_dra=[]
    j=0
    for i in range(len(y)):
        if y[i] in dra and Checkcouple(y[j:i]):
            y_splited.append(y[j:i])
            y_dra.append(y[i])
            j=i+1
    y_splited.append(y[j:])
    return y_splited,y_dra
def Convert(l):
    l1_splited,l1_dra=drasplit(l,'+-')#先按+-分割
    l2_splitedsum,l2_drasum=[],[]
    for k in l1_splited:#再按*/分割
        l2_splited,l2_dra=drasplit(k,'*/')
        l2_splitedsum.append(l2_splited)
        l2_drasum.append(l2_dra)
    for m in range(len(l2_splitedsum)):
        for n in range(len(l2_splitedsum[m])):
            if l2_splitedsum[m][n][0]=='(':#去掉括号
                l2_splitedsum[m][n]=Convert(l2_splitedsum[m][n][1:-1])
    resultsum=''
    for a in range(len(l2_splitedsum)):#组合结果，组合运算符
        result=l2_splitedsum[a][0]+' '
        for b in range(len(l2_drasum[a])):
            result+=l2_splitedsum[a][b+1]+' '+l2_drasum[a][b]+' '
        if a==0:
            resultsum+=result
        else:
            resultsum+=result+l1_dra[a-1]+' '
    return resultsum[:-1]

l=input()
print(Convert(l))