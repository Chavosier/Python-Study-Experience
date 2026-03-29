'''
说明
编写python程序，统计英语短文中字母出现的次数，并输出出现次数最多的字母（如有多个均输出）和未出现的字母。要求字母不区分大小写，均表示为大写字母。（若有多个，以空格分隔输出）

数据格式
输入
一行，一个字符串

输出
出现次数最多的字母及其次数和未出现的字母

第一行为出现次数最多的字母

第二行为出现的次数

第三行为未出现的字母

样例
输入数据 1
Saying and doing are two different things.
输出数据 1
N
5
B C J K L M P Q U V X Z
'''
l=input()
l=l.upper()
Ha=[0]*26

for i in l:
    k=ord(i)-ord('A')
    if 0<=k<=25:
        Ha[k]+=1

m=0
mi=-1
for i in range(len(Ha)):
    if m<Ha[i]:
        m=Ha[i]
for i in range(len(Ha)):
    if m==Ha[i]:
        print(chr(i+ord('A')),end=' ')
print()
print(m)
for i in range(len(Ha)):
    if 0==Ha[i]:
        print(chr(i+ord('A')),end=' ')