from tkinter import*
from pygame import mixer
import time,pyttsx3
import pygame
e= pyttsx3.init()
root =Tk()
pygame.init()
mixer.music.load('background.wav')
mixer.music.play()
root.title("windows assistant")
root.configure(bg="blue")
def main():
    e.say("Wake up harsh its your time to play!.")
    e.runAndWait()
btn= Button(root,text= "Speak...",font= ('Helvetica',10),width= 30,height=4,bg='green',fg='white',command= main).pack()
root.geometry("700x300")

root.mainloop()