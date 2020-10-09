import sys
import socket
from datetime import datetime

from tkinter import *

window=Tk()

#def runpograme():
#
##    t1.insert(END,e1_value.get())
#    print(e2_value.get())
###    t3.insert(END,e3_value.get())
def scanb():
    a = e1_value.get()
    x = int(e2_value.get())
    y = int(e3_value.get())
    if len(a) == 2:
        target = socket.gethostbyname(a[1])

    print("-" * 50)
    print("------Kunal--Harpude------")
    print("scanner target " + a)
    print("time standard: " + str(datetime.now()))
    print("-" * 50)

    for port in range(x,y):
    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	socket.setdefaulttimeout(1)
    	result = s.connect_ex((a,port))
    	print("checking port {}".format(port))
    	if result == 0:

            alert_popup("This is result", "port {} is open".format(port) , "scan ccompleted")
            print("port {} is open".format(port))
    	s.close()
def alert_popup(title, message, path):
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
        # Examples

#alert_popup("This is result", "port {} is oprn".format(port) , "scan ccompleted")
ip_addr = Label(window,  text = "IP Address")
ip_addr.grid(row=0,column=0)

start_port = Label(window,  text = "Starting port")
start_port.grid(row=1,column=0)

End_port = Label(window,  text = "Ending port")
End_port.grid(row=2,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

#t1=Text(window,height=1,width=20)
#t1.grid(row = 0, column = 2,
#       columnspan = 2, rowspan = 2, padx = 5, pady = 5)

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=1,column=1)

#t2=Text(window,height=1,width=20)
#t2.grid(row=1,column=2)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value)
e3.grid(row=2,column=1)

#t3=Text(window,height=1,width=20)
#t3.grid(row=2,column=2)


b2=Button(window,text="Scan",command=scanb)
b2.grid(row=3,column=1)

window.mainloop()
