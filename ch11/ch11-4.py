# encoding:utf-8
# !/usr/bin/python
import sys

#导入Qt的类

from  PyQt4.QtGui import  QLabel,QApplication
#使用from import导入方式，所有的Qt对象均是以Q开头
App=QApplication(sys.argv)
#每个Qt应用程序都必须有且只有一个QApplication对象,QApplication的参数为sys.argv，便于程序处理命令行参数
Label=QLabel("hello world")
#QLabel是标签函数
Label.show()
#控件被创建时，默认是不显示的，必须调用show()函数来显示它。该过程与其他的GUI相似，需要调用show()函数才进行显示。
sys.exit( App.exec_()  )
#调用QApplication的exec_()方法，程序进入消息循环，等待可能输入进行响应。Qt完成事件处理及显示的工作，并在应用程序退出时返回exec_()的值。另外不要与python的exec的混淆。