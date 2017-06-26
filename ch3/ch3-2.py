# -*- coding: utf-8 -*-
a=dict((['mike','001'],['mary','002'],['john','003'],['tom','004'],['jenny','005'],['herry','006']))
b=raw_input('please input your name: ')
c=raw_input('please input your password: ')                                  
if (b in a) and c==a[b]:
        print u'欢迎 ',b



