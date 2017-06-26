# -*- coding: utf-8 -*-
import time
def decselect(sel):
     def startdec(func):
          def r(*t,**d):
               print u'下面调用函数：',func.__name__,u'开始调用时间为：',time.ctime()
               func(*t,**d)
          return r
     def enddec(func):
          def r(*t,**d):             
               func(*t,**d)
               print  u'函数：',func.__name__,u'于',time.ctime(),u'调用结束'
          return r
     try:
          return {'start':startdec,'end':enddec}[sel]
     except KeyError,e:
          raise ValueError(e),u'必须是“start”或“end”'
     
     
@decselect('start')
def sp(seq):
     '输出一个序列'
     for n in seq:
          print n,
     print

sp([1,2,3,4,5,6])



     
     
     






