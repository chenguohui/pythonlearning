# -*- coding: utf-8 -*-
myfile=open('D:/firstfile.txt','w+')
myfile.write('my first file built by python\n')
myfile.write('hello,world\n')
myfile.seek(0,0)
for eachline in myfile:
    print eachline,
myfile.close()

