def devide(x):#质因数分解
    a=[]
    j=2
    while x!=1:
        if x % j == 0:
            a.append(j)
            x= x // j 
            j-=1
        j+=1       
    if x != 1:
        a.append(x)
    return a
def delete_mix(x):#元素合并
    x.append(0)#若最后一个数会出现两次，则在最后添加一个0，保证不会漏掉。比如225=3*3*5*5，不加0，y=325（应为3252)
    y=''
    a=[]
    k=0#k为前一个数的个数
    for i in x:
        if i not in a:
            a.append(i)
            if k>1:
                y+=str(k)
            k=0
            y+=str(i)
        if i in a:
            k+=1
    return int(y[:-1])#去掉最后的0
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while i * i <= n:
        if n % (i-1) == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

# o=13532385396179
o=20
# flag=True
# while flag==True:
#     while True:
#         op=delete_mix(devide(o))
#         if op==o:
#             flag=is_prime(o)
#             break
#         else:
#             o=op
#     o+=1
while True:
    op=delete_mix(devide(o))
    print(op)
    if op==o:
        flag=is_prime(o)
        break
    else:
        o=op
print(flag)
