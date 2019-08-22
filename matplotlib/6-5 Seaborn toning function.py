__author__ = 'zhongyue'
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


# Seaborn简单画图(五) -- Seaborn调色功能

def sinplot():
    x = np.linspace(0,14)
    plt.figure(figsize=(8,6))
    for i in range(4):
        plt.plot(x,np.sin(x+i)*(i+0.75),label='sin(x+%s)*(%s+0.75)' %(i,i))
    plt.legend()

sinplot()
plt.show()

sns.set()
sinplot()
plt.show()


print(sns.color_palette())
sns.palplot(sns.color_palette())
plt.show()

# 自带风格
pal_style = ['deep', 'muted', 'pasted', 'dark', 'colorblind']
sns.palplot(sns.color_palette('dark'))
plt.show()

# 设置画板
sns.set_palette(sns.color_palette('dark'))
sinplot()
plt.show()


# 清空画板
print(sns.color_palette())
sns.set()
print(sns.color_palette())
sinplot()
plt.show()


# 局部使用画板with语句，外部还是系统画板
with sns.color_palette('dark'):
    sinplot()
plt.show()


# 外部没变
sinplot()
plt.show()


# 自定义画板
pall = sns.color_palette([(0.1,0.2,0.3),(0.9,0.3,0.6),(0.3,0.3,0.3)])
sns.palplot(pall)
plt.show()



# 自动生成画板
sc = sns.color_palette('hls', 10)
sns.palplot(sc)
sns.set_palette(sc)
plt.show()


sinplot()
plt.show()

