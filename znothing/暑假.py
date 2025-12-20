def I(z):#发现一局比分
    s1=0
    s2=0
    flag=False
    for i in range(len(z)):
        if z[i] == '0':
            s2+=1
        if z[i] == '1':
            s1+=1
        if (s1>=6 or s2>=6) and (s1>=s2+2 or s2>=s1+2):#获胜条件
            s=str(s1)+':'+str(s2)
            z=z[i+1:]#删去已比分局
            flag=True
            break
    if flag==False:#没有发现一局比分
        s = str(s1) + ':' + str(s2)
        z=[]
    return s,z
def J(z):#组合所有局比分
    sa=''
    while z!=[]:
        sa+='/'+I(z)[0]
        z=I(z)[1]
    return sa


ss=[]
b=input()#string input
a=list(b)
s=[]
for i in range(len(a)-2):#找到001
    if  a[i] == '0' and a[i+1] == '0' and a[i+2] == '1':
        s.append(i+2)
for j in s:
    a=list(b)
    a[j-1]='1'#修正错误
    ss.append(J(a))
for i in range(len(ss)):
    print(str(s[i]) + ' ' + str(ss[i]))
