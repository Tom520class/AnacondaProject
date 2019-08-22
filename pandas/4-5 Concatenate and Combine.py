__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Concatenate和Combine操作
# series中矩阵（array）的连接
arr1 = np.arange(9).reshape(3,3)
print(arr1)
arr2 = np.arange(9).reshape(3,3)
print(arr2)
print(np.concatenate([arr1,arr2]))
print(np.concatenate([arr1,arr2],axis=1))
# axis，默认为0，表示按列连接（增加行数），即将第二个矩阵的列依次连接到第一个矩阵的列的下面。如果axis=1，表示按行连接（增加列数）


# series的连接
s1 = Series([1,2,3], index=['X','Y','Z'])
s2 = Series([4,5], index=['A', 'B'])
print(s1)
print(s2)
print(pd.concat([s1,s2]))
print(np.concatenate([s1,s2]))
# 注意，这里使用的是pandas的方法concat，因为上边使用的numpy的concatenate方法不能讲index进行连接，只能连接values


# 更改连接方式
# 同样的，也有一个axis的参数，默认为0。当指定axis=1时，将增加列，即将形成一个dataframe，没有的值将会填充为NaN
print(pd.concat([s1,s2], axis=1))



# dataframe的连接
df1 = DataFrame(np.random.rand(4,3), columns=['X', 'Y', 'Z'])
print(df1)
df2 = DataFrame(np.random.rand(3,3), columns=['X', 'Y', 'A'])
print(df2)
print(pd.concat([df1,df2]))
# 没有值的地方将会填充为NaN
print(pd.concat([df1,df2],axis=1))



# Combine的意思为：填充，补充
# series的combine
s1 = Series([2,np.nan,4,np.nan], index=['A','B','C','D'])
print(s1)
s2 = Series([1,2,3,4], index=['A','B','C','D'])
print(s2)
print(s1.combine_first(s2))
# 从结果可看出，s1用s2中的值填充了其中对应为NaN的值。


# dataframe的combine
df1 = DataFrame({
        'X':[1,np.nan,3,np.nan],
        'Y':[5,np.nan,7,np.nan],
        'Z':[9,np.nan,11,np.nan],
        })
print(df1)
df2 = DataFrame({
        'A':[1,2,3,4],
        'Z':[np.nan,10,np.nan,12],
        })
print(df2)
print(df1.combine_first(df2))