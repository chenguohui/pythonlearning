#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
class MyFileLike(object):
    '''
    自定义一个类文件 (file-like )
    '''
    def __init__(self):
        self._container=""
    def write(self, content):
        self._container += content        
    def read(self):
        return     self._container
def myfileoper(infile,  outfile ):
    '''
    以任意的类文件对象为参数 ； 
    如果参数 是字符串 ，需要通过open函数打开类对象 。
    ''' 
    if type(infile)==str:
        _infile=open(infile)
    else :
        _infile=infile
    if type(outfile)==str:
        _outfile=open(outfile,"w")
    else : 
        _outfile=outfile
    for i in _infile :          
        _outfile.write(i)    
    return

if __name__=="__main__":
    _myfilelike=MyFileLike()
    myfileoper(__file__,_myfilelike)##读取本文件 ，写入到自定义的类文件中 
    print _myfilelike.read()
    testStringIO=StringIO.StringIO()
    testStringIO.write("\nhello test StringIo\n")
    testStringIO.seek(0)
    myfileoper(testStringIO,_myfilelike)## 以 StringIO为 测试 ； 
    testStringIO.close()
    print  _myfilelike.read()
    
