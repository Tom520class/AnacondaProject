__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# merge操作的原则
df1 = DataFrame({'key':['X','Y','Z'], 'data_set_1':[1,2,3]})
print(df1)
df2 = DataFrame({'key':['X','B','C'], 'data_set_2':[4,5,6]})
print(df2)

print(pd.merge(df1,df2))
# 如果两个dataframe的column都不相同，则会在merge的时候报错
# df1 = DataFrame({'key':['X','Y','Z'], 'data_set_1':[1,2,3]})
# print(df1)
# df2 = DataFrame({'key1':['A','B','C'], 'data_set_2':[4,5,6]})
# print(df2)
# print(pd.merge(df1,df2))


# 而当两个dataframe具有相同的column时，若两个column中没有相同的value，则会merge一个空的dataframe：
df1 = DataFrame({'key':['X','Y','Z'], 'data_set_1':[1,2,3]})
print(df1)
df2 = DataFrame({'key':['A','B','C'], 'data_set_2':[4,5,6]})
print(df2)
print(pd.merge(df1,df2))



# merge的其他参数
# one参数可以指定merge的列名：
df1 = DataFrame({'key':['X','Y','Z'], 'data_set_1':[1,2,3]})
print(df1)
df2 = DataFrame({'key':['X','B','C'], 'data_set_2':[4,5,6]})
print(df2)
print(pd.merge(df1,df2, on='key'))
# 如果指定了一个私有的column则会报错：
# print(pd.merge(df1,df2, on='data_set_1'))
# how参数用于指定merge时的操作。
df1 = DataFrame({'key':['X','Y','Z', 'X'], 'data_set_1':[1,2,3,4]})
print(df1)
df2 = DataFrame({'key':['X','B','C'], 'data_set_2':[4,5,6]})
print(df2)
print(pd.merge(df1,df2,how='left'))
# 指定how=left，就是让df1保留所有的行列数据，df2根据df1的行列进行补全。同理，right也可以指定。
print(pd.merge(df1,df2,how='outer'))
# outer就是how指定为left和right的结果的集合