'''
A产品3元一个，有20%的概率得奖，奖品为一元乐享券，再买一个A的话只用花1元，
求买一个A产品的平均价值。
'''
'''
假设买5次A产品，之后会有x次中奖，
现买5批，1批5次，25次，有5x次中奖，将每一批第一次中奖得到的A汇总得5个A，
即有5x=5+x
解得x=5/4=1.25
即平均价格为(25*3+5x)/(25+5x)=2.6
'''     
import random
import matplotlib.pyplot as plt
l=[]
def test(n):
    m=n
    prize=3
    total=0
    for i in range(n):
        total+=prize
        flag=True
        while flag:
            if random.random()<0.2:
                m+=1
                total+=1
            else:
                flag=False
    return(total/m)
n=1
while n<=6:
    t=test(10**n)
    l.append(t)
    n+=1  # 补充递增

# 绘图
plt.plot(range(1, 7), l, marker='o')
plt.xlabel('n (10^n 次模拟)')
plt.ylabel('平均价格')
plt.title('一元乐享模拟结果')
plt.grid(True)
plt.show()
print(l)