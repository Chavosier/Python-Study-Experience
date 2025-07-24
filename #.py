import random
N, T, x = map(int, input().split())
ss = []
for i in range(555):
    a = [0] * N
    for ii in range(x):
        while True:
            s = random.randint(0, N - 1)
            if a[s] == 0:
                a[s] = 1
                break


    for iii in range(T):
        b =a
        j =0
        while j < N:
            if a[j]:
                if j == 0:
                    if a[1] == 0:
                        b[1] = 1
                elif j == N - 1:
                    if a[N - 2] == 0:
                        b[N - 2] = 1
                else:
                    r = random.randint(0, 1)
                    n= j + 1 if r else j - 1
                    if a[n] == 0:
                        b[n] = 1
            j += 1
        a = b

    ss.append(sum(a))

print(max(ss), min(ss))
n=int(input().strip())
s=set()
for i in range(n):
    s.add(input().strip())
print(52 - len(s))