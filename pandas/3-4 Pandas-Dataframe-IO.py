__author__='zhongyue'
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import webbrowser
from io import BytesIO

#打开网址，里面有io操作的介绍
# link = 'http://pandas.pydata.org/pandas-docs/version/0.20/io.html'
# webbrowser.open(link)
# 从粘粘板读取数据
# df1 = pd.read_clipboard()
# 把数据放入到粘粘板中，数据可以直接粘粘到excel文件中
# df1.to_csv('../data/df1.csv')
# df1.to_csv('../data/df2.csv', index=False)
df2 = pd.read_csv('../data/df1.csv')
# df2 = np.genfromtxt(BytesIO(df2), delimiter=",")
pd.read_csv("../data/df2.csv")
print(df2)
# 转化为json格式
df3 = df2.to_json()
# 读取json
df4 = pd.read_json(df3)
print(df4)
# 转化为html格式
df5 = df2.to_html("../data/df2.html")
# 装换为excel格式
df6 = df2.to_excel('../data/df2.xlsx')


print("PPPPPPPPPPPPPP")


ts = pd.Series(np.random.randn(1000),
              index=pd.date_range('1/1/2000', periods=1000))

print(ts)
print(ts.index)
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                   columns=['A', 'B', 'C', 'D'])
df.to_csv('../data/foo.csv')
df1 = pd.read_csv('../data/foo.csv')
print(df1)
df.to_hdf('../data/foo.h5', 'df')
df2 = pd.read_hdf('../data/foo.h5', 'df')
print(df2)
df.to_excel("../data/foo.xlsx", sheet_name='Sheet1')
df3 =  pd.read_excel('../data/foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(df3)