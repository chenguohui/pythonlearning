# -*- coding: utf-8 -*-
def ftupdict(arg1,arg2,arg3=333,*arg4,**arg5):
     print 'formal args:'
     print 'arg1=',arg1
     print 'arg2=',arg2
     print 'arg3=',arg3
     print u'非关键字可变数量参数:'
     for eacharg in arg4:
          print eacharg,
     print u'关键字可变数量参数:'
     for eachargkey in arg5:
          print eachargkey,":",arg5[eachargkey]


     
     
     






