# encoding:utf-8 
# !/usr/bin/python
import pandas as pd
import numpy as np
from pandas import *
import  pandas.io.data  as web
import datetime
#series
s1 =pd.Series(np.random.randn(4),name ="Series data " , index=list('ABCD'))
sdata={"A":1,"B":2,"C":3,"D":4}
s2=pd.Series(sdata)
print s1,s2
print s1[0]
print s1['A']
print s1.describe()#常用统计功能
#dataframe
#列表或者元组构成的列表
df1 =pd.DataFrame( [[10,20,30,40  ],[23,34,45,56]],
                  columns=['number',"number2","number3","number3"]
                  ,index=['a','b' ])
#由Series构成字典形式
d={'one':Series([1,2,3],index=['a','b','c']),
    'two':Series([4,5,6,7],index=['a','b','c','d'])
    }
df2 =pd.DataFrame(d)
print  pd.DataFrame( [{'a': 1, 'b': 2, 'c': '3'},
                      {'a':2, 'b':1}, {'c':1}])#字典列表
#由列表构成的字典
df =  pd.DataFrame({'a':[1,3,5,7,], 'b':[2,4,6,8,]})

print df

#数据索引以及数据访问
print"元素值", df['a'][0]#结果为1 ,通过df['a']获取的Series，而后通过序列获得元素值
print "列",df['b']
print"列", df.loc[:,'b']
print'lie', df.iloc[1]
print df.ix[1],df.ix[:,'b'],df[1:1]#ix的行、列、元素 索引
df.index.name =u"行名"
df.columns.name =u"列名"
#有关索引操作
print  df.index[1],df.index.name,df.columns.name
print"索引值 ", df.index# index 与columns是不可更改的 ，保证了Index在不同数据结构之间的共享
print "列名",df.columns,df.keys()#二者相同
#所有元素值
print  "所有元素值", df.values  #获得
print df['a'].values.tolist()# 通过.values获的numpy.array,而后通过tolist()获的DataFrame的所有元素列表

#添加元素值，列表形式需要严格对齐原DataFrame的维数
df['ee'] =list((1,2,3,4))
df['foo'] = np.ones((4,2)).tolist()
df['foo2'] = np.ones((4,2)).tolist()
df['test1']=Series((1,5,0,),index=(1,2,0))
print df#

#操作
print df.describe()#汇总统计
print df.T#转置
print df.sum()

#group by

print "group by "
print df
#group by
df['t']=('a1','a1','a2','a2')
grouped =df.groupby(df['t'] )
for name ,group in grouped :#生成的group对象，通过迭代方式访问
    print name
    print group
#调用groupby的函数 进行均值等统计功能
print grouped.describe(),grouped.mean(),\
    grouped.max(),grouped.size(),\
    grouped.count(),grouped.std()

#stock
import tushare as ts
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']   #字体
pylab.mpl.rcParams['axes.unicode_minus'] = False     # ‘-’开关
stockdata =ts.get_hist_data('162411')[ 'close']    #一次性获取全部日k线数
stockdata.index=pd.to_datetime(stockdata.index)
#eia 网提供了原油价格表
oilurl='http://www.eia.gov/dnav/pet/hist_xls/RWTCd.xls'
#pandas提供了直接从本地/网上读取EXCEL文件的read_excel函数 。
oildata  = pd.read_excel(oilurl ,sheetname='Data 1',skiprows=1000,index_col=0)
oildata.columns =['Crude Oil']#更改列名
oildata['162411']=stockdata*80#放大80倍，图形显示直观
oildata.index.name=u"华宝油气与原油"#更改索引名字 ，matplotlib显示用
print oildata['2014-02-13':]#输出所有数据
oildata['2014-02-13':] .plot()
plt.show()


