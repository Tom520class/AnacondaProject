__author__='zhongyue'
# 股票市场分析实战之历史趋势分析


# 基本信息
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
# 股票数据的读取
import pandas_datareader as pdr

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns
# 是在使用jupyter notebook 或者 jupyter qtconsole的时候，调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候，可以直接在你的python console里面生成图像
# %matplotlib inlines
#time
from datetime import datetime

# 阿里巴巴的股票行情和亚马逊的股票行情
ba = open('../data/BABA.csv')
am = open('../data/AMZN.csv')
# 以第0行作为索引
alibaba = pd.read_csv(ba, index_col=0)
amazon = pd.read_csv(am,index_col=0)
# 显示前5行
print(alibaba.head())

plt.subplot(4,2,1)
# 阿里巴巴关盘价画图
alibaba['Adj Close'].plot(legend=True)
# plt.show()

plt.subplot(4,2,2)
# 交易量
alibaba['Volume'].plot(legend=True)
# plt.show()

plt.subplot(4,2,3)
# 对比两只股票的关盘价
alibaba['Adj Close'].plot(legend=True)
amazon['Adj Close'].plot(legend=True)
# plt.show()

plt.subplot(4,2,4)
# 绘制每一天股价变动情况
alibaba['high-low'] = alibaba['High'] - alibaba['Low']
alibaba['high-low'].plot()

plt.subplot(4,2,5)
# 计算每天关盘盈亏比例,每一天之间闭市的价格变化的图像：
# pct_change方法可以获取与前一行之间的差值
alibaba['daily-return'] = alibaba['Adj Close'].pct_change()
# alibaba['daily-return'].plot()
# 优化之后：
alibaba['daily-return'].plot(figsize=(10,4),linestyle='--',marker='o')


plt.subplot(4,2,6)
# 直方图和密度图 ：需要drop掉NAN的值，否则会报错
# sns.distplot(alibaba['daily-return'].dropna())
# 优化一下 :
sns.distplot(alibaba['daily-return'].dropna(), bins=100,color='purple')
plt.show()

