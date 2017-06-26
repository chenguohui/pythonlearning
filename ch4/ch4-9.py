# -*- coding: utf-8 -*-
def fdict(arg1,arg2,arg3=333,**arg4):
     print 'formal args:'
     print 'arg1=',arg1
     print 'arg2=',arg2
     print 'arg3=',arg3
     print 'the rest args:'
     for eachargkey in arg4:
          print eachargkey,":",arg4[eachargkey]
     
     
     






