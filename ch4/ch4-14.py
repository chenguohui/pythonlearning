# -*- coding: utf-8 -*-
#全局变量示例
base=5000 #创建全局变量
def salary():
     fuat=raw_input(u"是否满勤 'Y/N':")#创建局部变量
     if fuat.upper()=='Y': #访问局部变量
          return base+2000 #访问全局变量
     else:
          return base #访问全局变量
def ps():
     ys=salary() #创建局部变量
     print u'你的工资为' ,ys, #访问局部变量
     print u'包括基本工资',base,'元和满勤奖',ys-base #访问全局变量并和局部变量进行运算

     
     
                   


     
     
     






