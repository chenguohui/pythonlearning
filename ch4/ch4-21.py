# -*- coding: cp936 -*-
#导入numpy模块
import numpy as np
#导入scipy模块中的fftpack子模块
from scipy import fftpack
#设置采样点个数
N=1000
#设置采样时间间隔
t=1.0/200
#根据采样间隔和采样个数产生序列x
x=np.linspace(0.0,N*t,N)
#通过函数计算得到序列y
y=6*np.sin(2*np.pi*x)+0.2*np.cos(100*np.pi*x)+0.03*np.sin(120*np.pi*x)
#导入matplotlib的pyplot子库用于绘图
import matplotlib.pyplot as plt
#创建图表1
plt.figure(1)
#显示时域图像，如图4.2所示
plt.plot(x,y)
#对时域信号进行傅里叶变换，求得频域信号
yf=fftpack.fft(y)
#设置频域信号的显示区间和时间间隔
xf=np.linspace(0.0,1.0/(2.0*t),N/2)
#创建图表2
plt.figure(2)
#显示频域图像，如图4.3所示
plt.plot(xf,2.0/N*np.abs(yf[0:N/2]))
#显示图表1、2
plt.show()

