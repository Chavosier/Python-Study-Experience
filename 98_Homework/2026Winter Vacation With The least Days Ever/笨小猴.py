'''
NOIP2008」笨小猴
传统题
1000ms
256MiB
说明
笨小猴的词汇量很小，所以每次做英语选择题的时候都很头疼。但是他找到了一种方法，经试验证明，用这种方法去选择选项的时候选对的几率非常大！ 
这种方法的具体描述如下：假设maxn是单词中出现次数最多的字母的出现次数，minn是单词中出现次数最少的字母的出现次数，如果maxn-minn是一个质数，
那么笨小猴就认为这是个Lucky Word，这样的单词很可能就是正确的答案。
输入格式
输入只有一行，是一个单词，其中只可能出现小写字母，并且长度小于100。
'输出格式
输出共两行，第一行是一个字符串，假设输入的的单词是Lucky Word，那么输出“Lucky Word”，否则输出“No Answer”； 
第二行是一个整数，如果输入单词是Lucky Word，输出maxn-minn的值，否则输出0。
输入数据 1
【输入输出样例1】
error
【输入输出样例2】
olympic


输出数据 1
【输入输出样例1】
Lucky Word
2
【输入输出样例2】
No Answer
0


提示
【输入输出样例1解释】 单词error中出现最多的字母r出现了3次，出现次数最少的字母出现了1次，3-1=2，2是质数。 
【输入输出样例2解释】 单词olympic中出现最多的字母i出现了2次，出现次数最少的字母出现了1次，2-1=1，1不是质数。
'''
word=input()
letter={}
for i in word:
    if i not in letter:
        letter[i]=1
    else:
        letter[i]+=1
l=[]
for i in letter:
    l.append(letter[i])
max=max(l)
min=min(l)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if is_prime(max-min):
    print("Lucky Word")
    print(max-min)
else:
    print("No Answer")
    print(0)