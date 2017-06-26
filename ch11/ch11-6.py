#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from string import join
import sqlite3 as db
DAYS = {
	0:  u"星期一",
	1: u"星期二",
	2: u"星期三",
	3: u"星期四",
	4: u"星期五",
	5: u"星期六",
	6: u"星期天",
}
class Application(QtGui.QWidget):
    def __init__(self):
        super(Application, self).__init__()
        self.dbName = 'todolist.db'
        self.initDb()
        self.initUI()
    def initDb(self):
        cx = db.connect(self.dbName)
        cu=cx.cursor()
        cu.execute("""CREATE TABLE  if not exists todo (day INTEGER, h INTEGER,\
         m INTEGER, note VARCHAR(100), UNIQUE(day, h, m))""")
        cx.close()
    def findDay(self, day):
        con = db.connect(self.dbName)
        cur = con.cursor()
        cur.execute("SELECT h,m,note FROM todo WHERE day=%d" % day)
        data = cur.fetchall()
        while self.results.count() > 0:
            it = self.results.takeItem(0)
            self.results.removeItemWidget(it)
        for i in data:
            h = str(i[0])
            m = str(i[1])
            note = unicode(i[2])
            if int(i[0]) < 10:
                h = '0' + str(i[0])
            if int(i[1]) < 10:
                m = '0' + str(i[1])
            self.results.addItem(h + ':' + m + ' ' + note)
        self.results.show()
    def getDay(self):
        self.findDay(self.cb.currentIndex())
    def delRow(self):
        if len(self.results.selectedItems()):
            it = self.results.selectedItems()[0]
            i = self.results.row(it)
            it = self.results.takeItem(i)
            text = unicode(it.text())
            hm = text.split(' ')[0]
            d = int(self.cb.currentIndex())
            n = join(unicode(text).split(' ')[1:])
            h = int(hm.split(':')[0])
            m = int(hm.split(':')[1])
            print d, h, m, n
            self.deleteRow(d, h, m, n)
            self.results.removeItemWidget(it)
    def addRow(self):
        if not self.ib.isHidden():
            self.getInp()
            self.ib.setHidden(True)
            return
        self.ib.setHidden(False)
        self.ib.setText('Enter task here in "h:m some task" format')
    def getInp(self):
        text = unicode(self.ib.text())
        hm = text.split(' ')[0]
        d = int(self.cb.currentIndex())
        n = join(unicode(text).split(' ')[1:])
        h = int(hm.split(':')[0])
        m = int(hm.split(':')[1])
        print d, h, m, n
        self.insertRow(d, h, m, n)
        self.findDay(self.cb.currentIndex())
        self.ib.setHidden(True)
    def deleteRow(self, day, h, m, note):
        con = db.connect(self.dbName)
        cur = con.cursor()
        cur.execute("DELETE FROM todo WHERE		\
                day=%d AND h=%d			\
                AND m=%d AND note='%s';"	\
                % (day,h,m,note))
        con.commit()
    def insertRow(self, d, h, m, n):
        con = db.connect(self.dbName)
        cur = con.cursor()
        cur.execute("INSERT into todo(day,h,m,note) VALUES \
                (%d, %d, %d, '%s');" % (d, h, m, n))
        con.commit()

    def initUI(self):
		self.cb = QtGui.QComboBox(self)
		for k,v in DAYS.items():
			self.cb.insertItem(k,  (v))
		self.cb.currentIndexChanged.connect(self.getDay)
		self.bt = QtGui.QPushButton(self)
		self.bt.setText(u"添加新纪录")
		self.bt.setToolTip(u"""
		<html><head/><body><p>
		<span style=" font-weight:600; font-style:italic; text-decoration: underline;">添</span>加
		<span style=" vertical-align:super;">+</span><span style=" color:#aa0000;">Add</span>
		</p></body>
		</html>""")
		self.bt.clicked.connect(self.addRow)

		self.btDel = QtGui.QPushButton(self)
		self.btDel.setText(u"删除")
		self.btDel.setToolTip("Delete")
		self.btDel.clicked.connect(self.delRow)
		self.ib = QtGui.QLineEdit(self)
		self.ib.setHidden(True)
		self.ib.returnPressed.connect(self.getInp)
		self.results = QtGui.QListWidget(self)
		self.gbox = QtGui.QGridLayout(self)
		self.gbox.addWidget(self.cb)
		self.gbox.addWidget(self.bt)
		self.gbox.addWidget(self.btDel)
		self.gbox.addWidget(self.ib)
		self.gbox.addWidget(self.results)
		self.setLayout(self.gbox)
		self.setGeometry(300,300, 300, 300)
		self.setWindowTitle('PyQt ToDo List');
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Application()
	sys.exit(app.exec_())
if __name__ == '__main__':
	main()

