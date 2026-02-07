'''
Description
输入共2行，第1行输入字符串母串，第2行输入字符串子串。 对子串在母串中的位置进行匹配

Format
Input
输入共2行，第1行输入字符串母串，第2行输入字符串子串。 aabcdfbcd bcd

Output
依次输出子串在母串中匹配成功的位置，如果不存在匹配成功位置，则输出-1

Samples
输入数据 1
aabcdfbcd
bcd
输出数据 1
2,6
'''
l=input()
w=input()
def find(l,k):
    a=-1
    if len(l)<len(k):
        return a
    for i in range(len(l)-len(k)+1):
        s=[-1]
        for j in range(len(k)):
            if l[i+j]==k[j]:
                s.append(0)
            else:
                s.append(1)
                break
        if sum(s)==-1:
            a=i
            return a
    return a
a=find(l,w)
if a==-1:
    print(a)
else:
    ans=''
    al=0
    while a!=-1:
        ans=ans+str(a+al)+','
        # l=l[a+len(w):]
        # al+=a+len(w)
        '''
        if the input is
        ababab
        abab
        the above code will miss the answer'2', because the first abab was deleted, the second abab is not compelete
        '''
        l=l[a+1:]
        al+=a+1
        a=find(l,w)
    print(ans[:-1])