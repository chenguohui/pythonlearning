# -*- coding: utf-8 -*-
import time 
# 定义一个计时函数，其参数为一个函数，用于接收被装饰的函数 
def time_stt(func):    
    # 定义一个内嵌的包装函数,记录下函数开始时间和结束时间 
    def wrapper(*t,**d): 
        start = time.time() 
        func(*t,**d)         
        usetime=time.time()-start
        print u'执行函数',func.__name__,u'用时',usetime,'秒'
        
    # 将包装后的函数返回 
    return wrapper
print u'装饰无参数函数试验:'
@time_stt
def test(): 
    time.sleep(3)
    
test()
print
print u'装饰一个参数函数试验:'
@time_stt
def pr(n): 
    for i in range(n):
        print i,
    print
        
pr(4)
pr(n=6)
print
print u'装饰两个参数函数试验:'
@time_stt
def area(l,w):
    print u'面积为：', l*w

area(40,23)
area(w=23,l=40)



     
     
     






