'''
Description
小李注册邮箱时，该邮箱要求设置登录密码，设置的密码必须符合下面条件：

（1）密码长度不能少于8位，且不能超过12位

（2）密码中必须包含至少3种不同类型的字符。大写字母、小写字母、数字字符、其他可见字符（可见字符的ASCII值范围为：33-126）

Format
Input
输入若干行，每行为一个字符串（邮箱密码）

Output
检测每行字符串，即判断邮箱密码是否符合要求，若符合要求，则输出“YES”，否则输出“NO”

Samples
输入数据 1
H2?N64Aj
[26wv9,Q
B9$14G/uvaskdfjwrew@#qr
zX?}r2T
输出数据 1
YES
YES
NO
NO
'''
import sys
def check(x):

    if 8 <= len(x) <= 12:
        Ha=[0,0,0,0]
        for j in x:
            i=ord(j)
            if 97<=i<=122:
                Ha[0]=1
            elif 65<=i<=90:
                Ha[1]=1
            elif 48<=i<=57:
                Ha[2]=1
            elif 33<=i<=126:
                Ha[3]=1
        if sum(Ha)>=3:
            return True
        else:
            return False
    else:
        return False
for line in sys.stdin.readlines():
    line=line.strip('\n')
    if check(line)==True:
        print('YES')
    else:
        print('NO')


