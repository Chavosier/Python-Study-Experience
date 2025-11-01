'''
Description
输入的第一行是待加密明文文本； 输入的第二行是用于加密的密钥； 请你按下列要求进行加密： 按文本中字符出现的次序，依次对文本中的ASCII码字符进行加密，加密仅仅针对字母字符（大写字母或小写字母） 每个字母字符按密钥的次序寻找密钥中的数值，若密钥长度不够，则密钥循环取数。如： s1="Hello World!" a=[1,2,4,3] Igpop Arsnh!

Format
Input
输入的第一行是待加密明文文本； 输入的第二行是用于加密的密钥；

Output
按文本中字符出现的次序，依次对文本中的ASCII码字符进行加密，加密仅仅针对字母字符（大写字母或小写字母） 每个字母字符按密钥的次序寻找密钥中的数值，若密钥长度不够，则密钥循环取数。 输出加密后的密文。

Samples
输入数据 1
Hello World!
1,2,4,3
输出数据 1
Igpop Arsnh!
'''
l = input()
ans = ''
key = list(map(int, input().split(',')))
key_pos = 0

for ch in l:
    if 'a' <= ch <= 'z':
        k = key[key_pos % len(key)]
        ans += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
#加密仅针对字母字符
    elif 'A' <= ch <= 'Z':
        k = key[key_pos % len(key)]
        ans += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))

    else:
        ans += ch
    key_pos += 1
print(ans)
