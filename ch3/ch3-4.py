# -*- coding: utf-8 -*-
a=dict((['admin1','123'],['admin2','456'],['admin3','789']))
u=dict((['mike','001'],['mary','002'],['john','003'],['tom','004'],['jenny','005'],['herry','006']))
b=raw_input('please input your name: ')
c=raw_input('please input your password: ')                                  
if (b in a) and c==a[b]:
    print u'欢迎管理员 ',b
elif (b in u) and c==u[b]:
    print u'欢迎用户 ',b
else:
    print u'请输入正确的用户名和密码'



