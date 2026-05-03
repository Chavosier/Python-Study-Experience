'''
pick from '浙江新高考选考信息优化卷（三） 第15题'
'''
def insettm(t):
    '''
    t:要插入的链表元素，格式为[catogory, index]    
    '''
    t.append(-1)
    zsd=t[0]
    p=ctinfo[zsd][1]
    tk.append(t)
    if p==-1:
        ctinfo[zsd][0]=ctinfo[zsd][1]=len(tk)-1
    else:
        tk[p][2]=len(tk)-1
        ctinfo[zsd][1]=len(tk)-1
def deltm(t):
    '''
    t:要删除的链表元素，格式为[catogory, index]    
    '''
    zsd=t[0]
    p=ctinfo[zsd][0]
    if p==-1:
        return
    else:
        if tk[p][1]==t[1]:
            ctinfo[zsd][0]=tk[p][2]
            if ctinfo[zsd][0]==-1:
                ctinfo[zsd][1]=-1
        else:
            q=p
            p=tk[p][2]
            while p!=-1 and tk[p][1]!=t[1]:
                q=p
                p=tk[p][2]
            tk[q][2]=tk[p][2]
            if ctinfo[zsd][1]==p:
                ctinfo[zsd][1]=q
def show(zsd):
    '''
    zsd:要显示的链表种类
    '''
    p=ctinfo[zsd][0]
    while p!=-1:
        print(tk[p])
        p=tk[p][2]
tk=[['A',1,2],['B',2,3],['A',3,5],['B',4,-1],['C',5,-1]] # 链表数据
ctinfo={'A': [0, 2], 'B': [1, 3],'C': [4, 4],'D':[-1,-1]} # 链表头尾信息
op=input('please input operation：')
t=input('please input data：')
if op=='insert':
    insettm(t)
    show(t[0])
elif op=='delete':
    deltm(t)
    show(t[0])