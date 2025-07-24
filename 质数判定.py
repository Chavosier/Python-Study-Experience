import time
x=int(input())
time_start = time.time()
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True if n!= 1 else False  # 1 is not a prime number

#-----------------______________Anoher way to write the code of /质数判定.py _______________-------------#
def is_prime(n):
    #"""判断质数的函数
    #参数：n，整数
    #返回值：True表示n是质数，False表示n不是质数
    
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
print(is_prime(x))
time_end = time.time()
print("Time used:", time_end - time_start)
