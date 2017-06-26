# -*- coding: utf-8 -*-
def fargsex(a1,a2,a3,a4,a5=555):
     t=[a1,a2,a3,a4,a5]
     i=1
     for ta in t:
          print i, ta
          i=i+1
print u"默认参数没有对应实参"
fargsex('er','ty',4,'67')
print u"默认参数有对应实参"
fargsex('er','ty',4,'67',28)
print u"通过形参名传递参数时，默认参数没有对应实参"
fargsex(a3='er',a1=4,a2='67',a4='we')
print u"通过形参名传递参数时，默认参数有对应实参"
fargsex(a3='er',a5='ty',a1=4,a2='67',a4='we')






