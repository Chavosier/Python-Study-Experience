def del_drama(l):
    l=l.replace("，","")
    l=l.replace("。","")
    return l

ori=input()
ori=del_drama(ori)
n=int(input())
data=[]
for _ in range(n):
    t=input()
    t=del_drama(t)
    data.append(t)
asd=ori*2
for i in range(n):
    if data[i] in asd:
        print("Yes!")
    else:
        print("No!")
