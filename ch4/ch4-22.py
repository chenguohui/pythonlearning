# -*- coding: cp936 -*-
#导入numpy模块
import numpy as np
#设置采样点个数
N=1000
#设置采样时间间隔
t=1.0/200
#根据采样间隔和采样个数产生序列x
x=np.linspace(0.0,N*t,N)
#通过函数计算得到序列y
y=6*np.sin(2*np.pi*x)+0.2*np.cos(100*np.pi*x)+0.03*np.sin(120*np.pi*x)
#导入Scipy的signal子模块
from scipy import signal
#设计低通滤波器，通带的截止频率为0.05*f0，f0为采样频率，阻带的起始频率为0.2*f0，通带的最大增益为2dB，阻带的最小衰减为10dB。
b,a=signal.iirdesign(0.05,0.2,2,10)
#利用滤波器对信号y进行滤波，信号y见例5.5。
z=signal.lfilter(b,a,y)
#导入matplotlib的pyplot子库用于绘图
import matplotlib.pyplot as plt
#利用绿色画出原信号
plt.plot(x,y,'g')
#利用红色画出滤波后信号
plt.plot(x,z,'r')  
#显示图表
plt.show()

