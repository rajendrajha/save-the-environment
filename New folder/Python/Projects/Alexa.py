import time
import webbrowser
import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
import pyjokes

r= sr.Recognizer()
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)

def say(txt):
 engine.say(txt)
 engine.runAndWait()
 
def tk():
  try:
     with sr.Microphone() as source:
         print('Listening...')
         voice =r.listen(source)
         command= r.recognize_google(voice)
         command= command.lower()
         if 'play' in command:
           song = command.replace('play','')
           pywhatkit.playonyt(song)
         if 'wikipedia' in command:
           wiki = command.replace('wikipedia','')
           a=  wikipedia.summary(wiki, 3)
           say(a)
           print(a)
         if 'google' in command:
           say('Opening google')
           webbrowser.open('www.google.com')
         if 'youtube' in command:
           say('Opening youtube')
           webbrowser.open('www.youtube.com')
         if 'whatsapp' in command:
           say('Opening whatsapp')
           webbrowser.open('web.whatsapp.com')
         if 'gmail' in command:
           say('Opening gmail')
           webbrowser.open('www.gmail.com')
         if 'time' in command:
           xa= time.strftime("%I  "+   '%p'+'   and    '+'%M'+ 'minutes')
           say('the time is  '+xa )
         if 'joke' in command:
           x= pyjokes.get_joke()
           say(x)
         if 'name' in command:
           say("My real name is alexa, an assistant")
         if 'address' in command:
           say("I live in San fransico city of USA.")
         if 'goal' in command:
           say("My goal is to make you happy")
  except:
    return command

tk()


