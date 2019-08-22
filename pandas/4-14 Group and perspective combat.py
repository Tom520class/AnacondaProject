__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
# 分组和透视实战
df = pd.read_csv('../data/usa_flights.csv')
print(df.head())
# 获取延误时间top10
print(df.sort_values('arr_delay', ascending=False)[:10])
# 获取延误比例:有一个value_counts方法可以计算指定列中值出现的次数，例如：
print(df['cancelled'].value_counts())
# 要一个delayed列，这一列根据arr_delay列值的正负来表示是否延误
df['delayed'] = df['arr_delay'].apply(lambda x:x>0)
print(df)
# 计算延误和非延误航班的个数
print(df['delayed'].value_counts())
# 用除法来计算延误航班的比例
delay_data = df['delayed'].value_counts()
print(type(delay_data))
print(delay_data[1]/(delay_data[0]+delay_data[1]))

# 根据’unique_carrier和delayed这两列进行groupby
print(df.head())
delay_group = df.groupby(['unique_carrier','delayed'])
print(delay_group)
# 通过size方法来获取每个航空公司延误和非延误航班的个数
print(delay_group.size())

# 得到的结果是一个2级的series，现在可以把他转化成为dataframe
df_delay = delay_group.size().unstack()
print(df_delay)
df_delay.plot()
plt.show()
# 通过传入参数改变图形的样式
df_delay.plot(kind='barh', stacked=True, figsize=[16,6],colormap='winter')
plt.show()
# 透视表功能
fights_by_carrier = df.pivot_table(index='flight_date', columns='unique_carrier', values='flight_num', aggfunc='count')
print(fights_by_carrier.head())