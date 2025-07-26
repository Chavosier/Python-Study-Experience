import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv(r'C:\vscode_study\pandas\报名信息.csv')

#print(df)

# a=['数','物','化','英']
# for ii in a:
#     list = []
#     for i in range(1, 4):
#         s = 0
#         k = str(i) + '班'
#         df1 = df[df.班级 == k]
#         for j in df1.values:
#             if ii in j[3]:
#                 s += 1
#         list.append(s)
#     print(list)
#     plt.bar(range(1, 4), list)
#     plt.title(ii+'报名人数')
#     plt.xlabel('班级')
#     plt.ylabel('报名人数')
#     plt.show()

# for i in range(1, 4):
#     s = 0
#     k = str(i) + '班'
#     df1 = df[df.班级 == k]
#     for j in df1.values:
#         if ii in j[3]:

df3=df[df.数+df.英+df.物+df.化==4]
df3=df3.sort_values(by='班级')
df3=df3.groupby('班级').count()
print(df3)