'''利用数字大小比较代替True/False判断，简化代码
'''
dic={'+':1,'-':1,'*':2,'/':2}
l=list(input().split())
sta=[]
for i in l:
    if '0'<=i[0]<='9':
        sta.append([i,[-3]])
    else:
        y=sta.pop();x=sta.pop()
        if abs(min(x[1]))<dic[i]:
            x=['('+x[0]+')',[-3]]
        if abs(min(y[1]))<=dic[i]:
            y=['('+y[0]+')',[-3]]
        sta.append([x[0]+i+y[0],[dic[i]],max(dic[i],max(x[1]),max(y[1]))])
print(sta[0][0])