'''
说明
求出2－n（n小于等于1000000）之间的所有质数（素数） 
输入格式
输入说明： 无 
输出格式
输出说明： 一行一个素数
输入数据 1
输出数据 1
</p>
提示
'''
n=1000000
Hash=[True]*(n+1)
k=int((n+0.5)**(0.5))
for i in range(2, k+1):
    if Hash[i]:
        j=i+i
        while j<=n:
            Hash[j]=False
            j+=i
for i in range(2, n+1):
    if Hash[i]:
        print(i)