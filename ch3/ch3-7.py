# -*- coding: utf-8 -*-
n=input('please input the number: ')
m=n/2 # 因为一个数的最大真因数不可能大于其值的一半，所以初值设为n/2
while m>0:
    if n % m==0:
        print n,u'的最大真因数为',m
        break
    m=m-1

