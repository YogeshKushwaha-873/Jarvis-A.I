import random
import datetime
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import pyjokes
import os
import time
import sys
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour< 12:
        a = "Good morning sir!", "Good morning sir! ", "Hello sir Good Morning!", "O, Good morning sir! ", "O, good morning sir! ", "Wow! Welcome back yogesh sir! "
        speak(random.choice(a))
    elif hour>= 12 and hour< 18:
        b = "Good Afternoon sir! ", "Good Afternoon sir! ", "Hello sir Good Afternoon! ", "O, Good Afternoon sir! ", "Ohhhh, good Afternoon sir!", "Wow! Welcome back yogesh sir!"   
        speak(random.choice(b))
    
    else:
        c = "Good Evening sir!", "Good Evening sir!", "Hello sir Good Evening!", "O, Good Evening sir!", "O, good Evening sir!", "Wow! Welcome back yogesh sir!"
        speak(random.choice(c))
wishMe()
wel = "So, how can i help you sir!", "How can i help you sir", "Give me a command Sir", "Online and ready sir", "What can i do for you", "Please give me a command Sir"
speak(random.choice(wel)) 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        print(e)
        speak("Try to say again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query  = takeCommand().lower()
        print(query)

        if "play music" in query:
                music_dir = "D:\\Songs\\Songs"
                songs = os.listdir(music_dir)
                #rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
        
        if 'wikipedia' in query:
            speak("Searching on wiki")
            try:
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                
                speak("so, wikipedia says")
                speak(results)
                
            except:
                speak("Not available on wikipedia")
         
        if 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go' in query:
            f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
            speak(random.choice(f))
            break
        
        elif 'open google' in query or 'search on google' in query or 'type on google' in query:
            ak = "what should i search?", "please say the words you want to search for", "what would you like to search sir?", "I am typing, say what you want to search on google?"
            speak(random.choice(ak))
            h = takeCommand().lower()
            webbrowser.open(f"https://www.bing.com/search?q={h}")
            

        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            
         
        elif 'open web browser' in query or 'open a new tab of browser' in query or 'open a web browser' in query:    
            webbrowser.open("www.goolge.com")
            
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.bing.com/search?q={query}")
            speak("As your wish sir")

        elif "nothing" in query:
            speak("thanks for using me sir!, have a good day.")
            sys.exit()

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takeCommand()
            if "yes" in ch:
                
                os.system("shutdown /s /t 1")
            else:
                speak("ok sir")
        elif "play music" in query:
            speak("tell me the song name!")
            p = takeCommand()
            webbrowser.open(f"www.youtube.com{p}")
        elif "play" in query:
            query = query.replace("play", "")
            speak("Ok sir opening your desired song!")
            webbrowser.open(f"https://soundcloud.com/search?q={query}")    
        elif 'who are you' in query or "give me your introduction" in query:
            speak("Wait, i am introducing myself. My name is Jarvis, I am an Assistant made by python progarmming, i can do many works like playing music, opening progarms, opening youtube, searching on web and many more!")
        elif "who am i" in query:
            jh = "if you are speaking then, definately you are a human!", "You are yogesh!", "You are a human!", "I cant identify peoples with their vocies, may be you are yogesh or anybody with relation of yogesh!"
            speak(random.choice(jh))
        elif 'hello' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            speak(random.choice(gf))        