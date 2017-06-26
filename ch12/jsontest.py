# encoding:utf-8 
# !/usr/bin/python
'''  差异之处 
Python3中 增加Json模块，与simplejson相同 。 
urllib2 需从  urllib.request 导入 
reload函数被移到  imp模块中 。  
bytes与str转换
'''
import sys
try:
    import json
except ImportError:    
    import simplejson as json 

if sys.version > '3':
    PY3 = True    
    import urllib.request 
else:
    PY3 = False
    import urllib2
 
obj = ([1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)})
encodedjson = json.dumps(obj,indent=True)
print((repr(obj) ))
print (encodedjson)
decodejson = json.loads(encodedjson)
print((type(decodejson)))
print (encodedjson)

import sys
import imp
try:
    imp.reload(sys)
    #sys.setdefaultencoding('utf-8')
except NameError:
    from  imp import reload 
    imp.reload(sys) 
    
urlstr='http://data.bank.hexun.com/other/sogou/ratejson.ashx'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 

if PY3:
    req =  urllib.request.Request(urlstr, headers = headers)  
    fp = urllib.request.urlopen(req)   
else :
    
    req =  urllib2.Request(urlstr, headers = headers )
    fp = urllib2.urlopen(req)  
jsondata=fp.read()
if PY3:
#是Python3中bytes 与str是两个完全不相干类型 ，需要做数据转换   
    print((type(jsondata))) 
    data=(jsondata[jsondata.decode().index("{"):len(jsondata)-1]    ) 
    data1=data.decode('utf-8')  
    dd=json.loads(data1)  
else: 
   dd=json.loads(jsondata[jsondata.index("{"):len(jsondata)-1]  )
 
#print((dd['huilv']))
print((u"%s的汇率情况表\n######################\n"%(dd['time'])))
for i in dd['huilv']:
    print((u"%s汇率是:%s" %( i['name'],i['value'] )))
