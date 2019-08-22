__author__='zhongyue'


# 数据获取有很多途径：
# 通过爬虫主动获取
# 通过官方提供的接口获取
# 通过一些专门提供数据的网站获取


# 实战准备

# 一、获取数据的一个库Tushare
# Tushare获取数据
# https://www.cnblogs.com/DreamRJF/p/8660630.html
import tushare as ts
# 1、获取历史行情数据 get_hist_data(
"""" 数说明：
code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
start：开始日期，格式YYYY-MM-DD
end：结束日期，格式YYYY-MM-DD
ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
retry_count：当网络异常后重试次数，默认为3
pause:重试时停顿秒数，默认为0
返回值说明：
date：日期
open：开盘价
high：最高价
close：收盘价
low：最低价
volume：成交量
price_change：价格变动
p_change：涨跌幅
ma5：5日均价
ma10：10日均价
ma20:20日均价
v_ma5:5日均量
v_ma10:10日均量
v_ma20:20日均量
turnover:换手率[注：指数无此项])"""
data = ts.get_hist_data('300274', start='2019-01-01', end='2019-08-16')
# print(data.head(10))

# 另外一个获取历史数据的函数get_h_data()。
# 在不指定开始时间和结束时间时，该函数默认返回最近一年的日线数据，返回的数据与get_hist_data不同的是，该函数只返回开盘价（open）、最高价（high）、收盘价（close）、最低价（low）、成交量（volume）、成交金额（amount）六列 ，同样加上时间段也可以获取相应数据。


# 第三个获取历史数据的函数get_k_data()。
# 与前两个函数相比，这个函数获取数据的速度很明显要快很多，而且可以返回每一只股票从上市开始到当前交易日的所有日线数据，这个有点是前两个函数都不具备的，更重要的是，如果批量3000多只股票的数据，前两个都不如get_k_data()稳定

# 2、获取实时行情数据get_today_all()
"""返回值说明：

code：代码
name:名称
changepercent:涨跌幅
trade:现价
open:开盘价
high:最高价
low:最低价
settlement:昨日收盘价
volume:成交量
turnoverratio:换手率
amount:成交量
per:市盈率
pb:市净率
mktcap:总市值
nmc:流通市值
"""
# 一次性获取当前交易所有股票的行情数据（如果是节假日，即为上一交易日）
# df = ts.get_today_all()
# print(df.head(10))

# 3、获取历史分笔数据之：get_tick_data()
"""
参数说明：
code：股票代码，即6位数字代码
date：日期，格式YYYY-MM-DD
retry_count : int, 默认3,如遇网络等问题重复执行的次数
pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
"""
df1 = ts.get_tick_data('300274', date='2019-08-02')
print(df1)
# 获取个股以往交易历史的分笔数据明细，通过分析分笔数据，可以大致判断资金的进出情况。在使用过程中，对于获取股票某一阶段的历史分笔数据，需要通过加入交易日参数并append到一个DataFrame或者直接append到本地同一个文件里。历史分笔接口只能获取当前交易日之前的数据，当日分笔历史数据请调用get_today_ticks()
# 接口或者在当日18点后通过本接口获取。

# 获取当日历史分笔数据：get_today_ticks()
"""
参数说明：

code：股票代码，即6位数字代码
retry_count : int, 默认3,如遇网络等问题重复执行的次数
pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
返回值说明：
time：时间
price：当前价格
pchange:涨跌幅
change：价格变动
volume：成交手
amount：成交金额(元)
type：买卖类型【买盘、卖盘、中性盘】
"""
df = ts.get_today_ticks('300274')
# print(df.head(10))
# 获取当前交易日（交易进行中使用）已经产生的分笔明细数据。

print("999999999")

# 二、 使用finance.yahoo.com这个网站。这个网站常被用来进行金融股票数据的搜索。

import pandas_datareader as pdr
alibaba = pdr.get_data_yahoo('BABA')
print(alibaba.head())






