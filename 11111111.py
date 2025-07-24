import pandas as pd
import random
# a=[]
# len=100000
# for i in range(len):
#     r=random.randint(10,100)
#     first_digit = int(str(r)[0])
#     a.append(first_digit)
# #print(a)
a=[2.99792458e8,6.62607015e-34,1.054571817e-34,1.380649e-23,6.67430e-11,5.670374419e-8,3.741771852e-16,1.438776877e-2,7.2973525693e-3,1.66053906660e-27,6.02214076e23,1.602176634e-19,4.835978484e14,2.58128074665e4,9.2847646208e-24,3.1524512550e-26,1.25663706212e-6,8.85418781762039e-12,9.1093837015e-31,1.67262192369e-27,1.67492749802e-27]
for i in range(len(a)):
    def fir(x):
        s=int(str(int(a[i]))[x])
        return s
    for j in range(len(str(int(a[i])))):
        if fir(j)!=0:
            a[i]=fir(j)
            break


df = pd.DataFrame({'数列': a})
counts = df.groupby('数列')['数列'].count().reset_index(name='出现次数')
counts['比率'] = counts['比率'] = ((counts['出现次数']/len(a) * 100).round(2)).astype(str) + '%'

print(counts)
