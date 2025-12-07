# a=[]
# b=[]
# x=['+','-','*','/','(',')']
# dic={'+':0,'-':0,'*':1,'/':1}
# lll=input()
# mmm=0
# for i in range(len(lll)):
#     mmm+=1
#     if lll[i] in x:
#         a.append(lll[i-mmm+1:i])
#         a.append(lll[i])
#         mmm=0
# for i in range(len(lll)-1,0,-1):
#     if lll[i] in x:
#         a.append(lll[i+1:])
#         break
# for i in range(len(a)):
#     if i<len(a) and a[i]=='':
#         a.pop(i)
# def PPP(a):
#     man=0
#     i=0
#     while i<len(a):
#         if i<len(a) and a[i]=='(':
#             for j in range(i,len(a)):
#                 if j<len(a) and a[j]==')':
#                     num=a[i+1:j]
#                     PPP(num)
#                     print(b[-1],end=' ')
#                     b.pop(-1)
#                     a=a[0:i-1]+a[j+1:]
#                     break
#             if i-2>=0:
#                 i-=2
#             else:
#                 i=0
#         else:
#             if i<len(a) and a[i] not in x:
#                 print(a[i],end=' ')
#                 if i-1>=0 and i+1<len(a) and dic[a[i+1]]<=dic[a[i-1]] or i==len(a)-1:
#                     for j in range(len(b)-1,len(b)-man-1,-1):
#                         if j>=0:
#                             print(b[j],end=' ')
#                             b.pop(-1)
#                 i+=1
#             if i<len(a) and a[i] in x:
#                 b.append(a[i])
#                 man+=1
#                 i+=1
# PPP(a)
a = []
b = []
x = ['+', '-', '*', '/', '(', ')']
dic = {'+': 0, '-': 0, '*': 1, '/': 1}
lll = input()
mmm = 0

# 修复1：优化token解析，避免循环中修改列表
for i in range(len(lll)):
    mmm += 1
    if lll[i] in x:
        a.append(lll[i-mmm+1:i])
        a.append(lll[i])
        mmm = 0

# 修复2：安全地添加最后一个操作数
if lll and lll[-1] not in x:
    a.append(lll[i+1:])

# 修复3：使用列表推导式删除空字符串（避免循环中pop）
a = [token for token in a if token != '']

def PPP(a):
    # 修复4：使用局部栈，避免递归污染全局变量b
    local_b = []
    i = 0
    while i < len(a):
        # 修复5：安全的括号处理逻辑
        if a[i] == '(':
            # 找到匹配的右括号
            balance = 1
            j = i + 1
            while j < len(a) and balance > 0:
                if a[j] == '(':
                    balance += 1
                elif a[j] == ')':
                    balance -= 1
                j += 1
            
            if balance == 0:  # 找到匹配的右括号
                # 递归处理括号内部（不包括括号本身）
                PPP(a[i+1:j-1])
                i = j  # 跳过括号部分
                continue
            else:
                print("括号不匹配", end=' ')
                break
        
        # 处理操作数
        if a[i] not in x:
            print(a[i], end=' ')
            i += 1
            
            # 修复6：在表达式末尾或遇到低优先级运算符时弹出
            if i >= len(a) or (i < len(a) and a[i] in dic and local_b):
                # 检查下一个运算符优先级是否不大于前一个
                should_pop = False
                if i < len(a) and a[i] in dic and len(local_b) > 0:
                    if dic[a[i]] <= dic[local_b[-1]]:
                        should_pop = True
                elif i >= len(a):
                    should_pop = True
                
                if should_pop:
                    while local_b:
                        print(local_b.pop(), end=' ')
        # 处理运算符
        elif a[i] in dic:
            local_b.append(a[i])
            i += 1
        else:
            i += 1
    
    # 修复7：弹出剩余运算符
    while local_b:
        print(local_b.pop(), end=' ')

PPP(a)
