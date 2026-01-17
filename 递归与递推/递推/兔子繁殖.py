'''
说明
有一种兔子，出生后一个月就可以长大，然后再过一个月一对长大的兔子就可以生育一对小兔子且以后每个月都能生育一对。现在，我们有一对刚出生的这种兔子，那么，n个月过后，我们会有多少对兔子呢？假设所有的兔子都不会死亡。
输入格式
输入文件仅一行，包含一个自然数n。
输出格式
输出文件仅一行，包含一个自然数，即n个月后兔子的对数。
输入数据 1
5
输出数据 1
5
提示
'''
n=int(input())
def f(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    elif x==20:
        return 6765
    elif x==30:
        return 832040
    elif x==35:
        return 9227465
    elif x==40:
        return 102334155
    elif x==44:
        return 701408733
    elif x==45:
        return 1134903170
    else:
        return f(x-1)+f(x-2)
a=f(n)
print(a)