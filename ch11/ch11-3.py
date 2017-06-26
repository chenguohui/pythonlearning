# encoding:utf-8
#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.finance import quotes_historical_yahoo
import datetime
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
root = Tk.Tk()
date1 = datetime.date( 2013, 1, 1 )
date2 = datetime.date( 2013, 12, 12 )
def getInputs():
    try:
        tolN = int(StockCode.get())
    except:
        tolN = 000001
    if tolN<600000:
        tolN=StockCode.get()+'.sz'
    else :
        print u"仅支持深证"
    return tolN
def _redraw():
    _redraw.f.clf()
    quotes = quotes_historical_yahoo( getInputs(), date1, date2)
    if len(quotes) == 0:
        raise SystemExit
    dates = [q[0] for q in quotes]
    opens = [q[1] for q in quotes]
    fig =Figure(figsize=(5,4), dpi=100)
    ax = _redraw.f.add_subplot(111)
    ax.plot_date(dates, opens, '-')
    _redraw.canvas.show()
    _redraw.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

_redraw.f =Figure(figsize=(5,4), dpi=100)
_redraw.canvas = FigureCanvasTkAgg(_redraw.f, master=root)
button = Tk.Button(master=root, text='redraw', command=_redraw)
button.pack(side=Tk.BOTTOM)
Tk.Label(root, text=u"股票代码").pack(side=Tk.TOP)
StockCode = Tk.Entry(root)
StockCode.pack()
StockCode.insert(0,'000001')
_redraw()
Tk.mainloop()

