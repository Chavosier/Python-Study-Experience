'''
说明
如果一个数从左边读和右边读都是同一个数，就称为回文数，例如686就是一个回文数。编程求10到n 内所有的既是回文数同时又是素数的自然数。
输入格式
输入一行，只有一个整数n(10<n<=1000000)
输出格式
输出多行，每行一个符合要求的素数回文数
输入数据 1

200
输出数据 1

11
101
131
151
181
191
'''
def is_hw(x):
    s = str(x)
    return s == s[::-1]

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
for num in range(10, n + 1):
    if is_hw(num) and is_prime(num):
        print(num)