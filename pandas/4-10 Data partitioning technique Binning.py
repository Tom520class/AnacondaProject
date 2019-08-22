__author__ = 'zhongyue'
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

# 数据分箱技术Binning


# 对series进行分箱
score_list = np.random.randint(25,100,size=200)
print(score_list)
# 指定一个分箱原则，规定：0-59为不及格，59-70为一般，70-80为良好，80-100位优秀：
bins = [0,59,70,80,100]
# 利用pandas中的cut方法，指定分箱规则和对象，结果将获得一个Categories对象：
print(pd.cut(score_list, bins))
# 对于这个对象就可以使用pandas中的value_counts方法来统计各个段内数据的个数：
score_cut = pd.cut(score_list, bins)
print(score_cut)
print(pd.value_counts(score_cut))




print("))))))))))")
# 对dataframe分箱
df1 = DataFrame()
df1['Score'] = score_list
print(df1.head())
# 这里的pd.util.testing.rands(3) for i in range(200)可以生成200个随机3位字符串。
df1['student'] = [pd.util.testing.rands(3) for i in range(200)]
print(df1.head())
# 使用前面的bins标准对df1进行分箱，得到一个Categories 对象
print(pd.cut(df1['Score'], bins).head())
# 将这个对象作为新的一列加入df1中：
df1['categories'] = pd.cut(df1['Score'], bins)
print(df1.head())
# 可以看到，新加的一列是前面score值所处的区间。

# 指定label参数为每个区间赋一个标签：
df1['categories'] = pd.cut(df1['Score'], bins, labels=['Low','ok','good', 'great'])
print(df1.head())
