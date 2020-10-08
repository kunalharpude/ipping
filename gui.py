from tkinter import *

window=Tk()

def runpograme():

    print(e1_value.get())
    t1.insert(END,e1_value.get())
    print(e2_value.get())
    t2.insert(END,e2_value.get())
    print(e3_value.get())
    t3.insert(END,e3_value.get())



e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=1,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=2)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value)
e3.grid(row=2,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=2,column=2)

b1=Button(window,text="show",command=runpograme)
b1.grid(row=3,column=1)
b2=Button(window,text="Execute",command=runpograme)
b2.grid(row=3,column=2)

window.mainloop()
