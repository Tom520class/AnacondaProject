__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt


# 时间序列操作基础

# 生成数据
# 首先使用date_range来生成一个时间序列，然后在生成一个和它一样长的series：
t_range = pd.date_range('20170101', '20171231')
print(t_range)
print(t_range.size)
print(len(t_range))
s1 = Series(np.random.randn(len(t_range)), index=t_range)
print(s1)
# pandas对于时间序列的采样提供了一种更为便利的方法：resample，它可以指定采样的标准（按天、月等）
# s1_month = s1.resample('D').mean()
s1_month = s1.resample('M').mean()
# s1_month = s1.resample('Y').mean()
print(s1_month)

# bfill和ffill :这是resample的两个方法，用于数据的填充
# bfill是向上填充即将2017-01-01 01:00:00至2017-01-01 23:00:00的值都填充为2017-01-02 00:00:00的值
print(s1.resample('H').bfill())
# ffill是向下填充，即将2017-01-01 01:00:00至2017-01-01 23:00:00的值都填充为2017-01-01 00:00:00的值
print(s1.resample('H').ffill())

# 画图:时间序列数据适合画基于时间的曲线图，这里画一个模拟的股票数据曲线图：
# 创建一个每小时一个点的时间序列：
t_range = pd.date_range('2017-01-01','2017-12-31', freq='h')
print(t_range)
# 创建一个index为这个时间序列的空的dataframe：
stock_df = DataFrame(index=t_range)
print(stock_df.head())
# 然后向其中填充整形随机数，模拟两个公司的股价：
stock_df['BABA'] = np.random.randint(80,160, size=8737)
print(stock_df.head())
stock_df['Tencent'] = np.random.randint(30,80, size=8737)
print(stock_df.head())

# 使用plot()方法可以生成一个图像的对象：
stock_df.plot()
plt.show()
# 将之前的数据按周采样，保存在新的dataframe中：
weekly_df = DataFrame()
weekly_df['BABA'] = stock_df['BABA'].resample('w').mean()
weekly_df['Tencent'] = stock_df['Tencent'].resample('w').mean()
print(weekly_df.head())
weekly_df.plot()
plt.show()