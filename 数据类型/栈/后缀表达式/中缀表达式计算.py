def Checkcouple(x):
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
    y_splited=[];y_dra=[]
    j=0
    for i in range(len(y)):
        if y[i] in dra and Checkcouple(y[j:i]):
            y_splited.append(y[j:i])
            y_dra.append(y[i])
            j=i+1
    y_splited.append(y[j:])
    return y_splited,y_dra
def Cal(l):
    l1_splited,l1_dra=drasplit(l,'+-')
    l2_splitedsum,l2_drasum=[],[]
    for k in l1_splited:
        l2_splited,l2_dra=drasplit(k,'*/')
        l2_splitedsum.append(l2_splited)
        l2_drasum.append(l2_dra)
    for m in range(len(l2_splitedsum)):
        for n in range(len(l2_splitedsum[m])):
            if l2_splitedsum[m][n][0]=='(':
                l2_splitedsum[m][n]=Cal(l2_splitedsum[m][n][1:-1])
    resultsum=0
    for a in range(len(l2_splitedsum)):#组合结果，组合运算符
        result=int(l2_splitedsum[a][0])
        for b in range(len(l2_drasum[a])):
            if l2_drasum[a][b]=='*':
                result*=int(l2_splitedsum[a][b+1])
            else:
                result/=int(l2_splitedsum[a][b+1])
        if a==0:
            resultsum+=result
        else:
            if l1_dra[a-1]=='+':
                resultsum+=result
            else:
                resultsum-=result
    return resultsum
# geshu=int(input())
# dui=0
# re=''
# flagg=True
# for v in range(geshu):
#     it=list(input().split('='))
#     da=Cal(it[0])
#     if da==int(it[1]):
#         re+=','+str(v+1)+'.Yes'
#         dui+=1
#     else:
#         re+=','+str(v+1)+'.No'
#     if flagg:
#         re=re[1:]
#         flagg=False
# print(re)
# sss=dui/geshu*100
# print('%.0f' %sss )
