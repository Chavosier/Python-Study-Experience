# import pandas as pd
# n = int(input())
# l=[]
# for i in range(n):
#     li=list(map(int, input().split()))
#     l.append(li)
# df_l=pd.DataFrame(l)
# df_l.columns=['A','B','C']
# df_l['总分']=df_l['A']+df_l['B']+df_l['C']
# df_l['xu']=df_l.index+1
# df=df_l.sort_values(['总分','A','xu'],ascending=[False,False,True]).head(5)#排列
# df.index=range(1,6)
# for i in range(1,6):
#     print(str(df.at[i,'xu'])+'  '+str(df.at[i,'总分']))


n=int(input())
da=[]
for i in range(n):
    a,b,c = map(int, input().split())
    total = a + b + c
    da.append((total, a, i+1)) #存储
print(da)
da.sort(key=lambda x: (-x[0], -x[1], x[2]))
print(da)
t5=da[:5]
for i in range(5):
    l1= t5[i][2]
    l2= t5[i][0]
    print(str(l1)+' '+str(l2))


