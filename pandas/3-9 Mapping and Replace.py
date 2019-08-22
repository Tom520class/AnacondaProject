__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
# dataframe中增加一列
df1 = DataFrame({'城市': ['北京','上海','广州'], '人口': [1000,2000,1500]})
print(df1)
# 通过series增加
df1['GDP'] = Series([1000,2000,1500])
print(df1)
# dataframe中每一列都是一个series，所以增加一个series就是增加了一列。

# map方式
df2 = DataFrame({'城市': ['北京','上海','广州'], '人口': [1000,2000,1500]})

print(df2)
gdp_map = {'北京': 1000,'上海': 2000,'广州': 1500}
df2['GDP'] = df2['城市'].map(gdp_map)
print(df2)
# 这种方式的优点在于不用关心index，因为在gdp_map中已经指定了每一行对应的值，只需要按照城市将对应GDP插入即可。


# Series中的replace
s1 = Series(np.arange(10))
print(s1)
print(s1.replace(1,np.nan))
print(s1.replace({2:np.nan}))
# 第一个参数表示需要被替换的目标value，第二个参数表示替换成的值。

print(s1)
print(s1.replace([1,2,3],[1000,2000,300]))