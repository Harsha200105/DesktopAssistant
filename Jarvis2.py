#! usr/bin/env python3

import datetime
import getpass
import os
import random
import smtplib
import sys
import webbrowser
from pygame import mixer

import pyttsx3
import speech_recognition as sr
import wikipedia

print("Initializing Jarvis....")
MASTER = getpass.getuser()

engine = pyttsx3.init("nsss")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
}
search_engines = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "bing": "https://www.bing.com",
}

def speak(text):
    engine.say(text)
    engine.runAndWait()
    pass


def print_and_speak(text):
    print(text)
    speak(text)

def open_url(url):
    webbrowser.open(url)
    chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
    webbrowser.get(chrome_path).open(url)


def search(search_query, search_engine = search_engines["google"]):
    try:
        open_url(f"{search_engines[search_engine]}/search?q={search_query}")
    except :
        print_and_speak("An Error has occured.")


def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning" + MASTER)
    elif hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)

    # speak("Hey I am Jarvis. How may I help you")


# This is where our programme begins....


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    print("Recognizing....")
    query = ""
    try:
        query = r.recognize_google(audio, language="en-in")
        print("User said: " + query)

    except sr.UnknownValueError:
        print("Sorry could you please try again?")

    except Exception as e:
        print(e)
        print("Say that again, please?")

    return query
    
def add_music(path) :
	music = []
	os.path.normpath(path)
	for item in os.listdir(path) :
		try :
			if os.path.isdir(os.path.join(path, item)) :
				music.extend(add_music(os.path.join(path, item)))
			elif os.path.isfile(os.path.join(path, item)) :
				extensions = ["mp3", "ogg", "wav", "wma", "aac", "m4a", "flac"]
				file_ext = i.split(".")[-1]
				if file_ext in extensions :
					music.append(os.path.join(path, i))
		except :
			print(f"ignored {item}")
	return music
	
# Music Folder
music_folder = "Your_music_folder_path(absolute_path)"
music = add_music(music_folder)    

speak("Initializing Jarvis....")
wish_me()
query = take_command().lower()

# logic for executing basic tasks
if "wikipedia" in query.lower():
    speak("Searching wikipedia....")
    query = query.replace("wikipedia", "")
    print_and_speak(wikipedia.summary(query, sentences=2))

elif "what's up" in query or "how are you" in query:
    st_msgs = (
        "Just doing my thing!",
        "I am fine!",
        "Nice!",
        "I am nice and full of energy",
    )
    speak(random.choice(st_msgs))

elif "date" in query:
    print_and_speak(f"{datetime.datetime.now():%A, %B %d, %Y}")

elif "time" in query:
    print_and_speak(f"{datetime.datetime.now():%I %M %p}")

elif "open" in query.lower():
    website = query.replace("open", "").strip().lower()
    try:
        open_url(popular_websites[website])
    except IndexError:  # If the website is unknown
        print(f"Unknown website: {website}")
        speak(f"Sorry, I don't know the website {website}")

elif "search" in query.lower():
    search_query = query.split("for")[-1]
    search_engine = query.split("for")[0].replace("search", "").strip().lower()
    if search_engine in search_engines : 
    	search(search_query, search_engine)
    else :
    	search(search_query)

elif "email" in query:
    speak("Who is the recipient? ")
    recipient = take_command()

    if "me" in recipient:
        try:
            speak("What should I say? ")
            content = take_command()

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("Your_Username", "Your_Password")
            server.sendmail("Your_Username", "Recipient_Username", content)
            server.close()
            speak("Email sent!")
        except Exception:
            speak("Sorry Sir! I am unable to send your message at this moment!")

elif "nothing" in query or "abort" in query or "stop" in query:
    speak("okay")
    speak("Bye Sir, have a good day.")
    sys.exit()

elif "hello" in query:
    speak("Hello Sir")

elif "bye" in query:
    speak("Bye Sir, have a good day.")
    sys.exit()

elif "play music" in query:
    speak("Playing your request")
	mixer.init()
	try : 
		mixer.music.load(random.choice(music))
		mixer.music.set_volume(1.0)
		mixer.music.play()
	except :
		print("Format Not Supported")



speak("Next Command! Sir!")
