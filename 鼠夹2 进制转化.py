m2=input()
m2=list(m2)
sss=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
for i in range(len(m2)):
    if m2[i] =='1':
        m2=m2[i:]
        break
m2=''.join(m2)

a=4-(len(m2))%4
m2='0'*a+m2
print(m2)
def BH(x):
    x10=1*int(x[3])+2*int(x[2])+4*int(x[1])+8*int(x[0])
    x16=sss[x10]
    return str(x16)

p=''
for i in range(0,len(m2),4):
    q=BH(m2[i:i+4])
    p=p+q
if p[0]=='0':
    p=p[1:]
print(p)




