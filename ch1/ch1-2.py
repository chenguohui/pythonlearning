#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick 
from matplotlib.font_manager import FontProperties
import datetime
font = FontProperties(fname=r"C:/Windows/Fonts/msyh.ttf",size=18)
# 定义起始、终止日期和股票代码
date1 =  ( 2007, 11, 25 )
date2 = (2008,12,20)#datetime.datetime.now () 
stock_num = '601857.ss'#上海的为ss，深圳的为sz
# 定义日期格式
mondays = WeekdayLocator(MONDAY)
alldays = DayLocator() 
weekFormatter =  DateFormatter('%b %d') 
dayFormatter = DateFormatter('%d')   
# 获取股票数据
quotes = quotes_historical_yahoo(stock_num, date1, date2)
if len(quotes) == 0:
    raise SystemExit
fig, ax = plt.subplots()
#fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
candlestick(ax, quotes, width=0.6)
ax.xaxis_date()
ax.autoscale_view()
plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.title(u'中石油 2007 -2008',fontproperties=font)
plt.show()