'''
Background
如果一个自然数从左边读和从右边读都相同，都是指同一个数，我们就将其称为“回文数”。

Description
请你编写程序，从小到大输出所有k位的“回文素数”（既是“回文数”，同时又是“素数”的自然数）。

例如：272虽是回文数，但不是素数。而131则符合本题要求，既是回文数又是素数，因此是“回文素数”。

Format
Input
输入一个正整数k（1<=k<=6）

Output
从小到大，一行输出一个“回文素数”，要求输出所有k位的“回文素数”值，最后一行输出统计结果。

Samples
输入数据 1
1
输出数据 1
2
3
5
7
1位整数共有4个回文素数
输入数据 2
2
输出数据 2
11
2位整数共有1个回文素数
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
s=0
n = int(input())
for num in range(10**(n-1), 10**n):
    if is_hw(num) and is_prime(num):
        print(num)
        s+=1
print(str(n)+'位整数共有'+str(s)+'个回文素数')