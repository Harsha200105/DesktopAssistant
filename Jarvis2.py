import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import random

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
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif "what\'s up" in query or 'how are you' in query:
    stMsgs = ['Just doing my thing!', 'I am fine!',
              'Nice!', 'I am nice and full of energy']
    speak(random.choice(stMsgs))

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

elif 'email' in query:
    speak('Who is the recipient? ')
    recipient = takeCommand()

    if 'me' in recipient:
        try:
            speak('What should I say? ')
            content = takeCommand()

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("Your_Username", 'Your_Password')
            server.sendmail('Your_Username', "Recipient_Username", content)
            server.close()
            speak('Email sent!')

        except:
            speak('Sorry Sir! I am unable to send your message at this moment!')

elif 'nothing' in query or 'abort' in query or 'stop' in query:
    speak('okay')
    speak('Bye Sir, have a good day.')
    sys.exit()

elif 'hello' in query:
    speak('Hello Sir')

elif 'bye' in query:
    speak('Bye Sir, have a good day.')
    sys.exit()

elif 'play music' in query:
    music_folder = Your_music_folder_path
    music = [music1, music2, music3, music4, music5]
    random_music = music_folder + random.choice(music) + '.mp3'
    os.system(random_music)

    speak('Playing your request')

speak('Next Command! Sir!')
