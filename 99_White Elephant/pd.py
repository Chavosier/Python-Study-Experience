import pandas as pd
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'd'])
# s= s1 + s2
# print(s)
print(s1.plot(kind='bar'))

