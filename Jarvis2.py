import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis....")
MASTER = "Harsha"


engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()



def wishMe():
    hour = datetime.datetime.now().hour
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    # speak("Hey I am Jarvis. How may I help you")


# This is where our programme begins....

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    query = " "
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said: " + query)

    except sr.UnknownValueError:
        print("Sorry Could You please try again")

    except Exception as e:
        print(e)
        print("Say That Again Please")
        query = None

    return query


speak("Initializing Jarvis....")
wishMe()
query = takeCommand()

# logic for executing basic tasks
if 'wikipedia' in query.lower():
    speak('Searching wikipedia....')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)


elif 'open youtube' in query.lower():

    webbrowser.open("youtube.com")
    url = 'https://www.youtube.com/'

    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

elif 'on google' in query.lower():
    
    webbrowser.open("google.com")
    url = 'https://www.google.com/'

    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

# elif 'play music' in query.lower():
#     songs_dir = "//Users//bindu//Desktop//imusic"
#     songs = os.listdir(songs_dir)
#     print(songs)
#     os.open(os.path.join(songs_dir, songs[0]))
