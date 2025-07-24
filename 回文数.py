# import sys
#
# # 设置更大的限制
# sys.set_int_max_str_digits(10000)
#
# m=int(input())
# def dsa(x):
#     r=int(str(x)[::-1])
#     return r
# c=0
# while dsa(m)!=m and c<=10000000:
#     m=m+dsa(m)
#     c+=1
#     print(m)
# if c==11:
#     print("NO!")
# else:
#     print(c)
#     print(m)
def f2(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def f1(n):
    if n==n[::-1]:
        return True
    else:
        return False
k=int(input())
s=0
for i in range(10**(k-1),10**(k)):
    if f1(str(i)) and f2(i):
        print(i)
        s+=1
print(str(k)+"位整数共有"+str(s)+"个回文数")