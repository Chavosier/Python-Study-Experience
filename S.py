def is_weiwen(n):#判断是否为回文数
    if n==n[::-1]:
        return True
    else:
        return False
def is_rennian(n):#判断是否为闰年
    if (n%4==0 and n%100!=0) or n%400==0:
        return True
    else:
        return False
def strr(n):#改字符串，前面补零
    if 1<=n<=9:
        n='0'+str(n)
    else:
        n=str(n)
    return n
m0=input()
m=''
for i in m0:
    if i=='年':
        i1=m0.index(i)
    if i=='月':
        i2=m0.index(i)
    if i=='日':
        i3=m0.index(i)
m=m0[0:i1]+m0[i1+1:i2]+m0[i2+1:i3]#获取年月日总字符串
year=int(m0[0:i1]); month=int(m0[i1+1:i2]); day=int(m0[i2+1:i3])#获取年月日
flag=False
while not flag:
    if is_weiwen(m) == False:
        day += 1
        monthdays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if is_rennian(year) and month == 2:
            monthdays[2] = 29
        if day > monthdays[month]:
            month += 1#进位
            day = 1
        if month > 12:
            year += 1
            month = 1

        m =str(year)+strr(month)+strr(day)#year不用改，month和day需要补零
    else:
        print(strr(year) + '年' + strr(month) + '月' + strr(day) + '日')
        flag = True


#2001年10月01日






