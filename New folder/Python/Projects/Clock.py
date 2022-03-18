from tkinter import *
import time
root= Tk()
#("widthxHeight")
root.geometry("1000x150")

def clock():
   Hour= time.strftime('%H')
   Min= time.strftime('%M')
   Sec= time.strftime('%S')
   am_pm= time.strftime('%p')
   var1= (Hour+":"+Min+":"+Sec+" "+am_pm)
   var.config(text= var1)
   var.after(1000,clock)
var= Label(root, text = "", font= ("Helvetica",60))
var.pack()
clock()
root.mainloop
