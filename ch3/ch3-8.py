# -*- coding: utf-8 -*-
n=0
m=0
while m<=100:
    m=m+1
    if m % 3!=0 or m % 7!=0:
        continue
    n=n+1
print u'1~100中有',n,u'个数能被3和7同时整除'


    
    



