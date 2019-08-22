__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

# 数据聚合Aggregation
# 可以通过agg方法传入需要使用的聚合的函数，来对数据进行聚合：
df = pd.read_csv('../data/city_weather.csv')
g = df.groupby('city')
print(g.agg('min'))
print(g.agg('max'))

# 通过传入自定义的聚合函数来得到聚合的结果通过传入自定义的聚合函数来得到聚合的结果
def foo(attr):
    return attr.max() - attr.min()

print(g.agg(foo))