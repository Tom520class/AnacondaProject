__author__='zhongyue'
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series
data = {
    'Country': ['Belgium','India', 'Brazil'],
    'Capital':  ['Brussels', 'New Delhi', 'Brasiliz'],
    'Population': [11190864, 1303171035, 201847528]
}
s1 = Series(data['Country'])
print(s1)
print(s1.values)
print(s1.index)
s1 = Series(data['Country'], index=['A', 'B', 'C'])
print(s1)
print(s1.values)
print(s1.index)

print("_____________")
# dataFrame
df1 = DataFrame(data)
print(df1)
cou = df1['Country']
print(cou)
print(df1.iterrows())
for i in df1.iterrows():
    print(i),print(type(i)),print(len(i),print(type(i[1])))


s1 = Series(data['Capital'])
s2 = Series(data['Country'])
s3 = Series(data['Population'])
df_new = DataFrame([s1,s2,s3])
print(df_new)
df_new = df_new.T
print(df_new)
df_new = DataFrame([s1,s2,s3], index=['Capital','Country', 'Population' ])
print(df_new)
print(df_new.T)

# series可以看做一个一维的字典，而dataframe可以看作是一个二维的字典。