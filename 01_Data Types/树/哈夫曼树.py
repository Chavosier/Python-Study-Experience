'''
Description
有哈夫曼树具体描述如下：

img

现有若干个叶子节点，请计算由这些节点组建的哈夫曼树对应的带权路径长度值。

Format
Input
一行，输入若干个正整数，依次代表各个叶子节点的权值。

Output
计算由这些叶节点组成的哈夫曼树对应的带权路径长度值。

Samples
输入数据 1
2 4 5 8
输出数据 1
36
'''
data=list(map(int,input().split()))
data.sort()
ans=0
while len(data)>=2:
    x=data.pop(0)
    y=data.pop(0)
    ans+=x+y
    data.append(x+y)
    data.sort()
    # k=len(data)-1
    # while k>=1:
    #     if data[k-1]>data[k]:
    #         data[k-1],data[k]=data[k],data[k-1]
    #         k-=1
    #     else:
    #         break
print(ans)