#RRRRRGGBBBBBBC
s=input()
c= []
count = 1
for i in range(1, len(s)):
    if s[i]==s[i-1]:
            count += 1
    else:
        c.append(str(count)+s[i-1])
        count = 1
c.append(str(count)+s[-1])
print("".join(c))

