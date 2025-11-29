l=list(input().split());sta=[]
#sta中的元素都有两个状态，1代表该元素外层有加减法，2代表该元素外层有乘除法
for i in l:
    if '0'<=i[0]<='9':
        sta.append([i,False,False])
    else:
        y=sta.pop()
        x=sta.pop()
        if i in '+-':
            if y[1]:
                y[0]='('+y[0]+')'
                y[1],y[2]=False,False
            sta.append([x[0]+i+y[0],True,y[2] or x[2]])
        elif i in '*/':
            if x[1]:
                x[0]='('+x[0]+')'
                x[1],x[2]=False,False
            if y[1] or y[2]:
                y[0]='('+y[0]+')'
                y[1],y[2]=False,False
            sta.append([x[0]+i+y[0],False,True])
print(sta[0][0])
#后缀表达式很好地表现了运算顺序，代码与计算时类似