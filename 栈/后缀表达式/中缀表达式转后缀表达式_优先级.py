dic={'(':-3,'+':1,'-':1,'*':2,'/':2,')':0,'@':-1}
s=input()+'@'
sta=[0]*len(s)
tops=-1
opt=[0]*len(s)
topo=-1
t=""
for c in s:
    if c.isalnum():
        t+=c
    else:
        if len(t)>0:
            tops+=1;sta[tops]=t #type: ignore
            t=""
        if c=='(':
            topo+=1;opt[topo]=c #type: ignore
            continue
        if c==')':
            while opt[topo]!='(':
                b=sta[tops];tops-=1
                a=sta[tops];tops-=1
                op=opt[topo];topo-=1
                tops+=1;sta[tops]=a+' '+b+' '+op#type: ignore
            topo-=1
            continue
        if topo==-1 or dic[c]>dic[opt[topo]]:#type: ignore
            topo+=1;opt[topo]=c#type: ignore
            continue
        while topo!=-1 and dic[c]<=dic[opt[topo]]:#type: ignore
            b=sta[tops];tops-=1
            a=sta[tops];tops-=1
            op=opt[topo];topo-=1
            tops+=1;sta[tops]=a+' '+b+' '+op#type: ignore
        topo+=1;opt[topo]=c#type: ignore
print(sta[tops])