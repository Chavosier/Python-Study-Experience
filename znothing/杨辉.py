n=int(input())
s=[[1],[1,1]]
if n==1:
    print('1')
else:
    for i in range(3, n + 1):
        s0 = [0] * i
        s0[0] = 1
        s0[-1] = 1
        for j in range(1, i - 1):
            s0[j] = s[i - 2][j - 1] + s[i - 2][j]
        s.append(s0)
    for i in s:
        x = ''
        for j in i:
            x += str(j) + ' '
        x = x[:-1]
        print(x)