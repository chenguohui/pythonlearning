# encoding:utf-8 
import xlrd 
wb =xlrd.open_workbook('types.xls')
ws = wb.sheet_by_index(0)
wl=ws.col_values(0)
wln=wl[1:]
wln.sort()
print wln

