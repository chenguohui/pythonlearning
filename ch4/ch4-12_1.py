# -*- coding: utf-8 -*-
import time 
# 定义一个计时函数，其参数为一个函数，用于接收被装饰的函数 
def time_stt(func):    
    # 定义一个内嵌的包装函数,记录下函数开始时间和结束时间 
    def wrapper(): 
        start = time.time() 
        func()         
        usetime=time.time()-start
        print u'执行函数',func.__name__,u'用时',usetime,'秒' 
      
    # 将包装后的函数返回 
    return wrapper 
@time_stt  
def test(): 
    time.sleep(4)
test() 




     
     
     






