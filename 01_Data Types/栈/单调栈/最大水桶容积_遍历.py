'''
Description
小李想制作一个水桶，水桶的侧面由一整块完整的矩形铁皮构成，水桶底部材料不用考虑。 为了找出一块最合适的铁皮制作水桶侧面区域，小李用笔将铁皮划分成若干个相邻的矩形块，每个矩形块宽度均为1，高度为正整数（如下图所示）。

img

现请你编写程序帮助小李切割得到最适合的一整块矩形铁皮，要求用该铁皮制作的水桶容积尽可能大。

Format
Input
输入若干个连续矩形块的高度（这些矩形块宽度均为1）

Output
现请你编写程序找到最合适的连续矩形块来制作水桶，使得水桶容积尽可能大，输出水桶的容积。

说明：计算时pi=3.14，输出容积时保留1位小数。

Samples
输入数据 1
2 7 4
输出数据 1
3.9
'''
Vmax=0
pi=3.14
heights = list(map(int, input().split()))
def CalculateMaxV(a,b):
    l=b-a+1;hmin=heights[a]
    for i in range(a,b+1):
        if heights[i]<hmin:
            hmin=heights[i]
    V=(max(hmin,l)**2*(min(hmin,l)))/(4*pi)
    return V
l=1
while l<=len(heights):
    for a in range(len(heights)):
        if a+l-1<len(heights):
            b=a+l-1
            V=CalculateMaxV(a,b)
            if V>Vmax:
                Vmax=V
    l+=1
print('%.1f' %Vmax)        

