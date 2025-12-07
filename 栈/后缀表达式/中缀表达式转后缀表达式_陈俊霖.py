def F(data):
    z=[];c=[]
    for i in range(len(data)):
        z.append(data[i])
        if data[i-1]=='*' or data[i-1]=='/':
            a=z.pop();b=z.pop();d=z.pop()
            z.append(d+' '+a+' '+b)
    for i in range(len(z)):
        c.append(z[i])
        if z[i-1]=='+' or z[i-1]=='-':
            a=c.pop();b=c.pop();d=c.pop()
            c.append(d+' '+a+' '+b)
    return c.pop()
d=input();zhan=[];s=[];m=-1
for i in range(len(d)):
    m+=1
    if d[i]=='(':
        m=-1
        s.append(d[i])
    elif d[i-1]==')' and i>1:
        s.append(d[i])
        m=-1
    elif not '0'<=d[i]<='9':
        s.append(d[i-m:i])
        m=-1
        s.append(d[i])
if s[-1]!=')':
    s.append(d[i-m:i+1]) # type: ignore
for i in range(len(s)):
    zhan.append(s[i])
    if s[i]==')':
        zhan.pop();data=[];f=''
        while f!='(':
            f=zhan.pop()
            data.append(f)
        data.pop();data1=data[::-1]
        zhan.append(F(data1))
zhan=F(zhan)
for i in range(len(zhan)):
    print(zhan[i],end='')