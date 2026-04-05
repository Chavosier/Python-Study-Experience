'''
Description
在单一的密码表的基础上，维吉尼亚密码引入了一个26×26的英文字母方阵密表，如下图所示：

img

现在请你输入一串明文及密钥。

请你结合密钥，利用维吉尼亚方阵密表对明文进行加密。比如明文为“THEBOOKANDTHEPENCIL”，密钥为“BIG”，加密时，以明文为行，密钥为列，行和列交叉得到密文。

（1）若输入的明文中存在非字母字符，则不用进行加密。

（2）密钥均为英文字母字符，当密钥长度小于明文长度时，密钥可以循环使用。

请编写一个程序，输入明文和密钥，输出“维吉尼亚”密文。

Format
Input
第1行输入明文

第2行输入密钥

Output
借助维吉尼亚密码26×26的英文字母方阵密表，和题中提供的密钥，对该明文进行加密，输入加密后所得到的密文

Samples
输入数据 1
HELLO
KEY
输出数据 1
RIJVS
输入数据 2
HEd&QQ@LLoBF
KEY
输出数据 2
RIb&UO@PJyFD
Limitation
1s, 1024KiB for each test case.

说明：本题中处理的字母字符，若存在小写字母字符，加密方式与大写字母字符类似。
'''
face=input()
key=input()
hide=''
for i in face:
    if 'A'<=i<='Z':
        key=key.upper()
        hide+=chr((ord(i)-ord('A')+ord(key[0])-ord('A'))%26+ord('A'))
        
    elif 'a'<=i<='z':
        key=key.lower()
        hide+=chr((ord(i)-ord('a')+ord(key[0])-ord('a'))%26+ord('a'))
    else:
        hide+=i
    key=key[1:]+key[0]
print(hide)
