# -*- coding: utf-8 -*-
a=dict((['mike','001'],['mary','002'],['john','003'],['tom','004'],['jenny','005'],['herry','006']))
print u'请输入正确的用户名和密码,你3次输入机会'
b=raw_input('please input your name: ')
c=raw_input('please input your password: ')
n=1
while (b not in a) or c!=a[b]:
    n=n+1
    if n>3:
        print '3次输入错误，程序结束'
        break
    print u'你还有',4-n,'次输入机会,请输入正确的用户名和密码'
    b=raw_input('please input your name: ')
    c=raw_input('please input your password: ')
else:
    print u'欢迎 ',b

