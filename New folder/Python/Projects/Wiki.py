import wikipedia as wiki
from tkinter import *
import pyttsx3
import webbrowser as web
from googlesearch import search
root= Tk()
root.title("Google")


def speak(audio):
    engine = pyttsx3.init("sapi5")
    engine.say(audio)
    engine.runAndWait()


label= LabelFrame(root, text= 'Search Wikipedia',font=("Helvetica",60)).pack(pady= 10)
E1= Entry(label, font= ("Helvetica",30), width= 100)
E1.pack(pady=20,padx= 20)
label1= Frame(root)
label1.pack(pady=5)
text_scroll= Scrollbar(label1)
text_scroll.pack(side= RIGHT, fill= Y)
hor_scroll= Scrollbar(label1,orient= "horizontal")
hor_scroll.pack(side= BOTTOM, fill= X)
E2= Text(label1, yscrollcommand= text_scroll.set,wrap= "none", xscrollcommand= hor_scroll.set)
E2.pack()
text_scroll.config(command = E2.yview)
hor_scroll.config(command= E2.xview)
def oc2():
    E1.delete(0,END)
    E2.delete(0.0,END)
def oc():
    i= E1.get()
    for j in search(i, tld="co.in", num=10, stop=10, pause=2):
        oc2()
        E2.insert(0.0,j)
        print (j)
        web.open(j)



btn= Button(label, text= "Search",font= ("Helvetica",30),command= oc).pack(pady= 5, side= LEFT)
btn1= Button(label, text= "Clear",font= ("Helvetica",30),command=oc2).pack(pady= 5, side= RIGHT)
btn3= Button(label, text= "Speak",font= ("Helvetica",30)).pack(pady= 5, side= RIGHT)
root.mainloop()
