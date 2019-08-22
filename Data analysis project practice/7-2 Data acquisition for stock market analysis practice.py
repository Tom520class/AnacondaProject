__author__ = 'zhongyue'

# 股票市场分析实战之数据获取

# 获取历史数据
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

# start = datetime(2015,9,20)
# alibaba = pdr.get_data_yahoo('BABA',start=start)
# amazon = pdr.get_data_yahoo('AMZN', start=start)
# alibaba.to_csv("../data/BABA.csv")
# amazon.to_csv("../data/AMZN.csv")

start1= datetime(2015,1,1)
company = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB']
top_tech_df = pdr.get_data_yahoo(company, start=start1)['Adj Close']
top_tech_df.to_csv('../data/top5.csv')
