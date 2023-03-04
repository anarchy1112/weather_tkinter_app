import tkinter
from tkinter import *

win = Tk()
win.geometry("385x430")
win.wm_title('Weather forecast app')

hours=IntVar(value=3)
days=IntVar(value=1)
current=IntVar(value=12)

l1=Label(win, text="Choose period for which you want weather forecast", width=38, padx=3)
l1.place(x=10, y=10)

b1 = Radiobutton ( win, text='3h',variable=hours, value=3, state='normal')
b1.place(x=10, y=40)

b2 = Radiobutton ( win, text='6h', variable=hours, value=6)
b2.place(x=10, y=80)

b3 = Radiobutton ( win, text='9h', variable=hours, value=9)
b3.place(x=10, y=120)

b4 = Radiobutton ( win, text='12h', variable=hours, value=12)
b4.place(x=10, y=160)

b5 = Radiobutton ( win, text='1d', variable=days, value=1)
b5.place(x=130, y=40)

b6 = Radiobutton ( win, text='2d', variable=days, value=2)
b6.place(x=130, y=80)

b7 = Radiobutton ( win, text='3d', variable=days, value=3)
b7.place(x=130, y=120)

b8 = Radiobutton ( win, text='4d', variable=days, value=4)
b8.place(x=130, y=160)

b9 = Radiobutton ( win, text='Current', variable=current, value=12)
b9.place(x=250, y=40)

lb1=Listbox(win, width=20)
lb1.place(x=10 , y=210)

lb2=Listbox(win, width=20)
lb2.place(x=130 , y=210)

lb3=Listbox(win, width=20)
lb3.place(x=250 , y=210)


btn=Button(win, text='Show me', width=15, bd=4, pady=2, padx=2)
btn.place(x=135, y=390)


win.mainloop()