def Checkcouple(x):
    flag_checkcouple=True
    sta_checkcouple=[];top=-1
    for i in x:
        if i=='(':
            sta_checkcouple.append('@');top+=1
        elif i==')':
            if top==-1:
                flag_checkcouple=False
                break
            else:
                sta_checkcouple.pop();top-=1
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
def Convert(l):
    l1_splited,l1_dra=drasplit(l,'+-')
    l2_splitedsum,l2_drasum=[],[]
    for k in l1_splited:
        l2_splited,l2_dra=drasplit(k,'*/')
        l2_splitedsum.append(l2_splited)
        l2_drasum.append(l2_dra)
    for m in range(len(l2_splitedsum)):
        for n in range(len(l2_splitedsum[m])):
            if l2_splitedsum[m][n][0]=='(':
                l2_splitedsum[m][n]=Convert(l2_splitedsum[m][n][1:-1])
    resultsum=''
    for a in range(len(l2_splitedsum)):
        result=l2_splitedsum[a][0]+' '
        for b in range(len(l2_drasum[a])):
            result+=l2_splitedsum[a][b+1]+' '+l2_drasum[a][b]+' '
        if a==0:
            resultsum+=result
        else:
            resultsum+=result+l1_dra[a-1]+' '
    return resultsum[:-1]
def ArcConvert(l):
    l=list(l.split())
    sta_arcconvert=[]
    for i in l:
        if '0'<=i[0]<='9':
            sta_arcconvert.append([i,False,False])
        else:
            y=sta_arcconvert.pop()
            x=sta_arcconvert.pop()
            if i in '+-':
                if y[1]:
                    y[0]='('+y[0]+')'
                    y[1],y[2]=False,False
                sta_arcconvert.append([x[0]+i+y[0],True,y[2] or x[2]])
            elif i in '*/':
                if x[1]:
                    x[0]='('+x[0]+')'
                    x[1],x[2]=False,False
                if y[1] or y[2]:
                    y[0]='('+y[0]+')'
                    y[1],y[2]=False,False
                sta_arcconvert.append([x[0]+i+y[0],False,True])
    return sta_arcconvert[0][0]
while True:
    try:
        l=input()
        l_copy=l
        l=Convert(l)
        l=ArcConvert(l)
        print(l==l_copy)
    except:
        print('Null')
        break