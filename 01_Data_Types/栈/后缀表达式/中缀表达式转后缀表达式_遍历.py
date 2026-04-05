dic={'+':'a','-':'b','*':'c','/':'d'}
def find(y):
    list = [(len(y) if (v := y.find(c)) == -1 else v) for c in '()*+/-']
    return min(list)
def base(dra_pos,x):
    j=dra_pos+find(x[dra_pos+1:])+1
    i=dra_pos-find(x[:dra_pos][::-1])-1
    x=x[:i+1]+x[i+1:dra_pos]+' '+x[dra_pos+1:j]+' '+dic[x[dra_pos]]+x[j:]
    return x
def split(x, op1, op2):
    while x.find(op1) != -1 or x.find(op2) != -1:
        if x.find(op1) != -1 and x.find(op2) != -1:
            dra_pos = min(x.find(op1), x.find(op2))
        else:
            dra_pos = max(x.find(op1), x.find(op2))
        x = base(dra_pos, x)
    return x
l='('+input()+')'
while (R_pos:=l.find(')'))!=-1:
    L_pos=R_pos-l[:R_pos][::-1].find('(')-1
    l=l[:L_pos]+split((split(l[L_pos:R_pos+1], '*', '/')),'+','-')[1:-1]+l[R_pos+1:]
print(l.replace('a','+').replace('b','-').replace('c','*').replace('d','/'))
#以运算逻辑顺序转换中缀表达式为后缀表达式
'''
dic = {'+': 'a', '-': 'b', '*': 'c', '/': 'd'}#转换字典

def find(y):
    lst = [(len(y) if (v := y.find(c)) == -1 else v) for c in '()*+/-']
    return min(lst)

def base(dra_pos, x):
    j = dra_pos + find(x[dra_pos + 1:]) + 1
    i = dra_pos - find(x[:dra_pos][::-1]) - 1
    x = x[:i + 1] + x[i + 1:dra_pos] + ' ' + x[dra_pos + 1:j] + ' ' + dic[x[dra_pos]] + x[j:]
    return x

def split(x, ops):
    while any(x.find(op) != -1 for op in ops):
        dra_pos = min((x.find(op) for op in ops if x.find(op) != -1))
        x = base(dra_pos, x)
    return x

def Convert_WithoutTreat(x):
    x = split(x, '*/')
    x = split(x, '+-')
    return x[1:-1]

l = '(' + input() + ')'
while (R_pos := l.find(')')) != -1:
    L_pos = R_pos - l[:R_pos][::-1].find('(') - 1
    l = l[:L_pos] + Convert_WithoutTreat(l[L_pos:R_pos + 1]) + l[R_pos + 1:]

print(l.replace('a', '+').replace('b', '-').replace('c', '*').replace('d', '/'))
'''
