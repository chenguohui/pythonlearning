# -*- coding: cp936 -*-
#����numpyģ��
import numpy as np
#���ò��������
N=1000
#���ò���ʱ����
t=1.0/200
#���ݲ�������Ͳ���������������x
x=np.linspace(0.0,N*t,N)
#ͨ����������õ�����y
y=6*np.sin(2*np.pi*x)+0.2*np.cos(100*np.pi*x)+0.03*np.sin(120*np.pi*x)
#����Scipy��signal��ģ��
from scipy import signal
#��Ƶ�ͨ�˲�����ͨ���Ľ�ֹƵ��Ϊ0.05*f0��f0Ϊ����Ƶ�ʣ��������ʼƵ��Ϊ0.2*f0��ͨ�����������Ϊ2dB���������С˥��Ϊ10dB��
b,a=signal.iirdesign(0.05,0.2,2,10)
#�����˲������ź�y�����˲����ź�y����5.5��
z=signal.lfilter(b,a,y)
#����matplotlib��pyplot�ӿ����ڻ�ͼ
import matplotlib.pyplot as plt
#������ɫ����ԭ�ź�
plt.plot(x,y,'g')
#���ú�ɫ�����˲����ź�
plt.plot(x,z,'r')  
#��ʾͼ��
plt.show()

