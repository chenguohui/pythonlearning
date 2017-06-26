# encoding:utf-8 
# !/usr/bin/python
from PyQt4.QtGui import  *
from  PyQt4.QtCore import *
import sys
App=QApplication(sys.argv)
b=QPushButton(u"按钮,点击退出")
b.show()
App.connect(b,SIGNAL('clicked()'),App,SLOT("quit()"))
App.exec_()
