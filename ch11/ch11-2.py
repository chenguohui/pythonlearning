# encoding:utf-8 
# !/usr/bin/pythonfrom Tkinter import *
import  Tkinter as Tk
root = Tk.Tk()
def eventhandler(event):
    print "点击坐标", event.x, event.y
frame = Tk.Frame(root, width=100, height=100)
frame.bind("<Button-1>", eventhandler)
frame.pack()
root.mainloop()