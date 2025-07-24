import math
import pandas as pd

def safe_eval(expression):
    allowed_vars = {'math': math}
    try:
        return eval(expression, {"__builtins__": None}, allowed_vars)#“eval”是一个函数，它会将字符串作为代码来执行
    except:
        return None

# 用户输入
user_input = input("请输入数学表达式: ").strip().lower()
m =int(input('请输入限度: '))
# 处理输入中的 "pi"（替换为 math.pi）
if 'pi' in user_input:
    user_input = user_input.replace('pi', str(math.pi))

# 计算并存储结果到 n
n = safe_eval(user_input)

if n is None:
    print("无法解析表达式")
else:
    a = []
    for i in range(1, m+1):
        q = n * i
        w = q - int(q)
        a.append(w)
    s=pd.DataFrame(a)
    s1=s.sort_values(0, ascending=[True])
    s2=s.sort_values(0, ascending=[False])
    # print(s1)
    # print(s2)
    min_index1=s1.index[0]+1;min_index2=s2.index[0]+1   # 因为原循环从 i=1 开始
    min_value1=s1.iloc[0, 0];min_value2=s2.iloc[0, 0]#index as coumt,value as coparis
     #找到value最小的value的index
    min_val = {True:min_value1, False:(1-min_value2)}[min_value1< (1-min_value2)]
    min = {True:min_index1, False:min_index2}[min_value1< (1-min_value2)]
    N=min*n
    N=int(round(N, 0))
    print('近似值: '+str(N)+'/'+str(min))
    print('误差: '+str(min_val))
