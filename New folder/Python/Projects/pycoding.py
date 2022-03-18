from tkinter import*
import webbrowser
pycode= Tk()
pycode.configure(bg='green')
pycode.title("window 11 assitant for you all")
def i():
    webbrowser.open('www.google.com')
def j():
    webbrowser.open('www.youtube.com')
def f():
    webbrowser.open('web.whatsapp.com')
def o():
    webbrowser.open('https://education.minecraft.net/en-us/homepage')

b= Button(pycode,text = 'chrome',command= i,width=100).pack()
b= Button(pycode,text = 'yotube',command= j,width=100).pack()
b= Button(pycode,text = 'whatsapp',command= f,width=100).pack()
b= Button(pycode,text = 'minecraft',command= o,width=100).pack()
pycode.mainloop()
