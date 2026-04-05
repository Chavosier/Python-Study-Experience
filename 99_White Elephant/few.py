def is_prime(n):
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
def is_hw(n):
    if int(str(n)[::-1]) == n:
        return True
    else:
        return False
for i in range(11, 10000):
    if is_prime(i) and is_hw(i):
        print(i)