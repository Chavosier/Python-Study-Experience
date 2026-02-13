def is_prime_fast(n: int) -> bool:
    """确定性 Miller-Rabin，适用于 n < 3,317,044,064,679,887,385,961,981"""
    if n < 2:
        return False
    # 小质数表
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    
    # 将 n-1 写成 d * 2^s 的形式
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # 对于 n < 3e18，测试这些底数足够
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
n=int(input())
print(is_prime_fast(n))