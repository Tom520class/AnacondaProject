__author__='zhongyue'
# 股票市场分析实战之风险分析


# 基本信息
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
# 股票数据的读取
import pandas_datareader as pdr

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# 是在使用jupyter notebook 或者 jupyter qtconsole的时候，调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候，可以直接在你的python console里面生成图像
# %matplotlib inlines
#time
from datetime import datetime


# 多只股票的关盘价分析
f = open('../data/top5.csv')
top_tech_df = pd.read_csv(f, index_col=0)
# 对时间进行从前到后排序
top_tech_df = top_tech_df.sort_index()
print(top_tech_df.head())
# 获取每日股价变动情况 ,关盘价盈亏比
top_tech_dr = top_tech_df.pct_change()

# 价格走势图
top_tech_df.plot()
# 这里因为时间index为正序，所以图像都是上涨的。
plt.show()

# 选取其中3只
top_tech_df[['GOOG', 'MSFT', 'AAPL']].plot()
plt.show()

# 相关性分析, 每日变化散点图
# sns绘图scatter表示散点图，传入x，y轴，数据源top_tech_dr
sns.jointplot('AAPL','AMZN', top_tech_dr, kind='scatter')
# 可以看到在以（0,0）为分割的坐标中，1,3象限所在点比较多，而且相关性也比较强
# 通过这个图可以看出，阿里和亚马逊股价具有相关性，你涨我也涨。
plt.show()

# seaborn还有一个方法pairplot可以绘制出所有情况的散点图 ,画出全部列的散点图
sns.pairplot(top_tech_df.dropna())
# 可以看到散点图约符合一条直线则相关度越高。
plt.show()

# 分位数评估风险
# 使用盈亏比数据分析
# 0.48的几率盈利0.0011451358415861537
print(top_tech_dr['AAPL'].quantile(0.52))

# 0.90的几率亏损0.01479911393874036
print(top_tech_dr['GOOG'].quantile(0.1))
# 0.90的几率盈利434.5490142822266
print(top_tech_df['AMZN'].quantile(0.1))
# 微软MSFT这个股票来说，有95%的信心它的每日收益为-0.02158425705917303美元。
print(top_tech_dr['MSFT'].quantile(0.05))