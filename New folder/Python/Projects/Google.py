import sys
import pyttsx3
import speech_recognition as sr
import wikipedia
engine= pyttsx3.init()
r= sr.Recognizer()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
def say(txt):
    engine.say(txt)
    engine.runAndWait()

while True:
    try:
        from googlesearch import search
        with sr.Microphone() as source:
            say("Ask anything.")
            voice =r.listen(source)
            query= r.recognize_google(voice)
            query= query.lower()

            if "don't want" in query:
                sys.exit()

    except:
        pass
    for i in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(i)
    a= wikipedia.summary(query,4)
    say(a)

