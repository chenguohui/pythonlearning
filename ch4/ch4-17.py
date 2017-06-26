# -*- coding: utf-8 -*-
def curve(a,b,c):
     def cur(x):
          return a*x*x+b*x+c
     return cur
curve1=curve(2,1,1) #求具体a、b、c所对应的曲线
print[(x,curve1(x)) for x in range(5)]#利用列表解析求曲线ax^2+bx+c的多个坐标值
x=input(u'请输入x的值：')
print (x,curve1(x)) #根据用户输入的x值，求所对应坐标值



     
     
                   


     
     
     






