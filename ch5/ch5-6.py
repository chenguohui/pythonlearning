# encoding:utf-8 
from datetime import date,time,datetime
from decimal import Decimal
from xlwt import Workbook
wb = Workbook()
ws = wb.add_sheet('Type examples')
ws.write(0,0,u'第一列为数字数据')
ws.write(1,0,3.145)
ws.write(2,0,2<<40)
ws.write(3,0,Decimal('3.65'))
ws.write(4,0,date(2009,3,18))
ws.write(5,0,datetime(2009,3,18,17,0,1))
ws.write(6,0,time(17,1))

ws.write(0,1,'Text') 
ws.write(1,1,False)
ws.write(2,1,True)
wb.save('types.xls')
