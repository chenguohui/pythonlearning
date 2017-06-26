# -*- coding: cp936 -*-
#����numpyģ��
import numpy as np
#����scipyģ���е�fftpack��ģ��
from scipy import fftpack
#���ò��������
N=1000
#���ò���ʱ����
t=1.0/200
#���ݲ�������Ͳ���������������x
x=np.linspace(0.0,N*t,N)
#ͨ����������õ�����y
y=6*np.sin(2*np.pi*x)+0.2*np.cos(100*np.pi*x)+0.03*np.sin(120*np.pi*x)
#����matplotlib��pyplot�ӿ����ڻ�ͼ
import matplotlib.pyplot as plt
#����ͼ��1
plt.figure(1)
#��ʾʱ��ͼ����ͼ4.2��ʾ
plt.plot(x,y)
#��ʱ���źŽ��и���Ҷ�任�����Ƶ���ź�
yf=fftpack.fft(y)
#����Ƶ���źŵ���ʾ�����ʱ����
xf=np.linspace(0.0,1.0/(2.0*t),N/2)
#����ͼ��2
plt.figure(2)
#��ʾƵ��ͼ����ͼ4.3��ʾ
plt.plot(xf,2.0/N*np.abs(yf[0:N/2]))
#��ʾͼ��1��2
plt.show()

