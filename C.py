A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=A+B
C.sort(key=lambda x:-x)
s=''
for i in range(len(C)):
    s=s+str(C[i])+' '
print(s[:-1])


