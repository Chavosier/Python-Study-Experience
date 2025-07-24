def prime_factors(n):
    factor = 2
    factors = []
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n //= factor
        else:
            factor += 1
    return factors


# 读取用户输入
n = int(input("请输入一个正整数: "))

# 获取质因数列表
factors = prime_factors(n)

# 输出质因数分解表达式
print(f"{n}={'*'.join(map(str, factors))}")
