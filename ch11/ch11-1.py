# encoding:utf-8 
# !/usr/bin/python
from Tkinter import  *
root =Tk()
mylabel=Label(root,text="Hello World")
mylabel.pack()
root.mainloop()

from Tkinter import  *
root =Tk()
def callfunction():
    print " button  hello"
def callfunctionwithParm(a):
    print "hello",a
Button(root,text="With parm",command=lambda:callfunctionwithParm("parm")).pack()

Button(root, text="Change", command=callfunction).pack()

root.mainloop()