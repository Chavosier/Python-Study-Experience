import pandas as pd
#import matplotlib.pyplot as plt

# read the data into a pandas dataframe
df = pd.read_csv('食堂就餐数据.csv')
print(df)
df=df.groupby(['窗口编号','班级'], as_index=True).agg({'金额': ['mean', 'max']})
a=df.at
print(df)
# df['位置']=''
# for i in range(df.index[-1]+1):
#     if df.at[i,'窗口编号']<=2:
#         df.at[i,'位置']='1'
#     elif df.at[i,'窗口编号']<=4:
#         df.at[i,'位置']='2'
#     elif df.at[i,'窗口编号']<=5:
#         df.at[i,'位置']='3'
# #print(df)
# a={'1':0,'2':0,'3':0}
# df=df.groupby('位置').sum()
# for j in range(1,4):
#     j=str(j)
#     a[j]=df.at[j,'金额']
# #print(a['1'])
# plt.bar(a.keys(),a.values())
# plt.title('各窗口就餐金额')
# plt.xlabel('窗口编号')
# plt.ylabel('金额')
# plt.show()