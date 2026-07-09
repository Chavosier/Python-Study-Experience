# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:52:00 2026

@author: Chavosier
"""

# ========== Church 布尔值（thunk 版本）==========
TRUE_T  = lambda t: lambda f: t(None)
FALSE_T = lambda t: lambda f: f(None)

# ========== Church 数 ==========
ZERO  = lambda g: lambda x: x
ONE   = lambda g: lambda x: g(x)
TWO   = lambda g: lambda x: g(g(x))
THREE = lambda g: lambda x: g(g(g(x)))
FOUR  = lambda g: lambda x: g(g(g(g(x))))
FIVE  = lambda g: lambda x: g(g(g(g(g(x)))))

# ========== 基本运算 ==========
SUCC = lambda n: lambda g: lambda x: g(n(g)(x))
ADD  = lambda m: lambda n: lambda g: lambda x: m(g)(n(g)(x))
MUL  = lambda m: lambda n: lambda g: lambda x: m(n(g))(x)

# ========== 判零（返回 thunk 版本布尔）==========
is_Zero_T = lambda n: n(lambda x: FALSE_T)(TRUE_T)

# ========== 前驱函数（配对技巧）==========
PAIR   = lambda x: lambda y: lambda f: f(x)(y)
FIRST  = lambda p: p(lambda x: lambda y: x)
SECOND = lambda p: p(lambda x: lambda y: y)

NEXT = lambda p: PAIR(SECOND(p))(SUCC(SECOND(p)))
PRED = lambda n: FIRST(n(NEXT)(PAIR(ZERO)(ZERO)))

# ========== Y 组合子 ==========
Y = lambda f: (lambda x: f(lambda v: x(x)(v)))(lambda x: f(lambda v: x(x)(v)))

# ========== 阶乘 ==========
F = lambda f: lambda n: is_Zero_T(n)(lambda _: ONE)(lambda _: MUL(n)(f(PRED(n))))

factorial = Y(F)

# ========== 转换与测试 ==========
def church_to_int(n):
    return n(lambda x: x + 1)(0)

a = factorial(THREE)
print(church_to_int(a))   # 6

# 测试 0~5 的阶乘
for i in range(6):
    n = ZERO if i == 0 else SUCC(ZERO) if i == 1 else SUCC(SUCC(ZERO)) if i == 2 else \
        SUCC(SUCC(SUCC(ZERO))) if i == 3 else SUCC(SUCC(SUCC(SUCC(ZERO)))) if i == 4 else \
        SUCC(SUCC(SUCC(SUCC(SUCC(ZERO)))))
    # 或者用辅助函数生成 Church 数
    def int_to_church(n):
        if n <= 0: return ZERO
        return SUCC(int_to_church(n - 1))
    
    n = int_to_church(i)
    result = factorial(n)
    print(f"{i}! = {church_to_int(result)}")