__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Series排序

# 按索引进行排序
s = Series([1,2,3], index=['a','c', 'b'])

# 对Series的索引进行排序，默认是升序
print(s.sort_index())

# 对索引进行降序排序
print(s.sort_index(ascending=False))

# 对Series的值进行排序，默认是按值的升序进行排序的
print(s.sort_values())

# 对Seires的值进行降序排序
print(s.sort_values(ascending=False))
# 对值进行排序的时候，无论是升序还是降序，缺失值（NaN）都会排在最后面。


print("PPPPPP")
# Series的排名
# 默认是根据值的大小进行平均排名
s = Series([1, 3, 2, 1, 6], index=["a", "c", "d", "b", "e"])
print(s)
print(s.rank())

# 根据值在数组中出现的顺序进行排名
print(s.rank(method='first'))





print("&"*6)
# DataFrame排序
# 按列的索引升序进行排序，默认按行，升序
a = np.arange(9).reshape(3,3)
data = DataFrame(a, index=['0','2','1'], columns=['c','a','b'])
print(data)
print(data.sort_index())
# 按列的索引按降序进行排序
print(data.sort_index(ascending=False))

# 按行升序的索引进行排序
print(data.sort_index(axis=1))

# 按指定列的值大小顺序进行排序
a = [[9,3,1],[1,2,8],[1,0,5]]
data = DataFrame(a, index=['0', '2', '1'], columns=['c', 'a', 'b'])
print(data)
print(data.sort_values(by='c'))
# 按指定行值进行排序
print(data.sort_values(by='0', axis=1))
# axis=1的意思是指定行索引

# DataFrame的排名

a = [[9, 3, 1], [1, 2, 8], [1, 0, 5]]
data = DataFrame(a, index=["0", "2", "1"], columns=["c", "a", "b"])
print(data)

# 默认按列进行排名
print(data.rank())
# 按行进行排名
print(data.rank(axis=1))
# method参数和ascending参数的设置与Series一样。
