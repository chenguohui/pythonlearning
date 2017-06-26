# encoding:utf-8 
# !/usr/bin/python
 
import numpy as np
import tables  as tb
import  datetime as dt
from tables import  *
from time import time

'''
row_des={
    'Date':tb.StringCol(26,pos=1),
    'No1':tb.IntCol(pos=2),
    'No2':tb.IntCol(pos=3),
    'No3':tb.Float64Col(pos=4),
    'No4':tb.Float64Col(pos=5)
    }
'''
#定义列描述符
class row_des(IsDescription):
    Date=tb.StringCol(26)
    No1=tb.IntCol()
    No2=tb.IntCol()
    No3=tb.Float64Col()
    No4=tb.Float64Col()
#
h5=tb.open_file('tab.h5','w',title='test pytable')
#创建表格
rows=20000
tab=h5.create_table('/','ints_floats',row_des,   title='ingeters and floats ', expectedrows=rows )
ran_int = np.random.randint(0, 10000, size=(rows, 2))
ran_flo = np.random.standard_normal((rows, 2)).round(5)
pointer =tab.row
for i in range(rows):
    pointer['Date'] = dt.datetime.now()
    pointer['No1'] = ran_int[i, 0]
    pointer['No2'] = ran_int[i, 1]
    pointer['No3'] = ran_flo[i, 0]
    pointer['No4'] = ran_flo[i, 1]
    pointer.append()
tab.flush()
print tab
group = h5.create_group("/", 'hdf5_group', 'group  infromation')
tab1=h5.create_table(group,'grouptable',row_des,title='group table')
row=tab1.row
for i in xrange(100):
    row['Date'] = dt.datetime.now()
    row['No1'] = ran_int[i, 0]
    row['No2'] = ran_int[i, 1]
    row['No3'] = ran_flo[i, 0]
    row['No4'] = ran_flo[i, 1]
    row.append()
tab1.flush()

#访问



# create array
arr_int = h5.create_array('/', 'integers', ran_int)
arr_flo = h5.create_array('/', 'floats', ran_flo)

print "访问数据"
print h5

print tab[:3]
print h5.root.ints_floats[:3]
print h5.root.hdf5_group.grouptable[2]['Date']#行号 列号
print  h5.root.integers[1:10]

print h5.root.ints_floats[:]['No1'].max()
#for i  in  h5.root.integers:
    #print i
h5.close()