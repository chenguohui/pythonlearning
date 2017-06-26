# coding=utf-8

import re 
from bs4 import BeautifulSoup
import sys
if sys.version > '3':
    PY3 = True
else:
    PY3 = False
'''
reload(sys)
sys.setdefaultencoding('utf-8')
'''
 
if PY3:
    import urllib.request
    text=urllib.request.urlopen('http://www.sse.com.cn/assortment/fund/etf/diclosure/volumn/').read() 
else :
    import urllib2
    #text = urllib2.urlopen('http://www.sse.com.cn/assortment/fund/etf/diclosure/volumn/').read()
    text=urllib2.urlopen('http://www.sse.com.cn/market/funddata/volumn/etfvolumn/').read() 
#text=open(r'./ETF.html').read()
mysoup = BeautifulSoup(text,"html.parser")
print(mysoup.original_encoding)#显示text的编码 

#print (mysoup.prettify)
print (mysoup.title) 
print (mysoup.title.name )
print (mysoup.title.get_text() )
print (mysoup.title.attribute)
 

print (mysoup.link)
print (mysoup.link['href'])
print (mysoup.link['rel'])
print (mysoup.link['type'])

 

tags= mysoup.find_all('link')
 
for tag in tags:
    print("href=", tag['href'],"rel=",mysoup.link['rel'],"type=", mysoup.link['type'])

 
 
 
##table
print ("table" )
tables=mysoup.find_all("table",class_="tablestyle")  
for table in tables:
    for row in table .find_all("tr")  :
        for tr in row.find_all("td") : 
           print (re.sub("\s","",tr.get_text()))#去掉空
testdata="""
 <div class="icon_col">
        <h1 class="h1user">123</h1>
        <h1 class="h1user1">456</h1>
        <h1 class="h1user2">789</h1>
</div>
"""
mysouptest=BeautifulSoup(testdata)
mysoupdata1=mysouptest.find_all('h1',class_='h1user')
 
print( mysoupdata1 )
mysoupdata2 = mysouptest.findAll(name="h1", class_=re.compile(r"h1user(\s\w+)?") )
print( mysoupdata2 )
for mydata in mysoupdata2:
	print (mydata.attrs ,mydata.text )
 
