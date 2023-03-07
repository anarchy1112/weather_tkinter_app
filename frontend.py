import tkinter
from tkinter import *

import backend

win = Tk()
win.geometry("535x500")
win.wm_title('Weather forecast Novi Sad app')


def current_weather_command():
    lb3.delete(0,END)
    for row in backend.current_weather():
        lb3.insert(END, row)

    lb2.delete(0,END)
    for row in backend.daily_forecast(h):  #pogledaj šta json daje i koriguj vrednosti sati i dana, takođe vidi šta koji lb prikazuje
        lb2.insert(END, row)

    lb1.delete(0,END)
    for row in backend.hourly_forecast(days.get()):
        lb1.insert(END, row)


hours=IntVar(value=1)
days=IntVar(value=8)
current=IntVar(value=12)
h=hours.get()

l1=Label(win, text="Choose period for which you want weather forecast", width=38, padx=3)
l1.place(x=10, y=10)

b1 = Radiobutton ( win, text='3h',variable=hours, value=1, state='normal')
b1.place(x=10, y=40)

b2 = Radiobutton ( win, text='6h', variable=hours, value=2)
b2.place(x=10, y=80)

b3 = Radiobutton ( win, text='9h', variable=hours, value=3)
b3.place(x=10, y=120)

b4 = Radiobutton ( win, text='12h', variable=hours, value=4)
b4.place(x=10, y=160)

b5 = Radiobutton ( win, text='1d', variable=days, value=8)
b5.place(x=180, y=40)

b6 = Radiobutton ( win, text='2d', variable=days, value=16)
b6.place(x=180, y=80)

b7 = Radiobutton ( win, text='3d', variable=days, value=24)
b7.place(x=180, y=120)

b8 = Radiobutton ( win, text='4d', variable=days, value=32)
b8.place(x=180, y=160)

b9 = Radiobutton ( win, text='Current', variable=current, value=12)
b9.place(x=340, y=40)

lb1=Listbox(win, width=30)
lb1.place(x=10 , y=210)

lb2=Listbox(win, width=30)
lb2.place(x=180 , y=210)

lb3=Listbox(win, width=30)
lb3.place(x=340 , y=210)


btn=Button(win, text='Show me', width=15, bd=4, pady=2, padx=2, command=current_weather_command)
btn.place(x=195, y=390)

btn2=Button(win, text='Close', width=15, bd=4, pady=2, padx=2, command=win.destroy)
btn2.place(x=195, y=430)


win.mainloop()