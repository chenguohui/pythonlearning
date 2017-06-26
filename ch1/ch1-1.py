#! /usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt #与Matlab区别，在Python环境下使用，必须引入Matplotlib包
import matplotlib as mpl
myfont = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttf')  
#mpl.rcParams['font.sans-serif'] =['SimHei']# ['SimHei']# ['SimHei'] #指定默认字体
plt.plot([-2,2,3,4,5],'r',label=u'第一条曲线')#颜色为 红色的曲线 
plt.plot([3,4,5,8,9],'b',label=u'第二条曲线')#颜色为蓝色
plt.legend () 
#plt.legend((u'第一个曲线',u'第二个曲线') )#可通过lengend函数指定legend
plt.grid(True) 
plt.axis([0   ,5,-3,9]) #坐标轴的 最大值与最少值 
plt.xlabel(u'X轴坐标  ',fontproperties=myfont)# 坐标轴标签  
plt.ylabel(u'Y轴坐标',fontproperties=myfont) 
plt.title(u' matplotlib 演示图 ',fontproperties=myfont) 
plt.show()
plt.savefig('plot123.png') #保存图形 
