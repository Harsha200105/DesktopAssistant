import datetime
import random
import smtplib
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia
from pygame import mixer

import gui

mixer.init()

print("Initializing Jarvis....")
MASTER = "Tony Stark"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "GitHub": "https://www.github.com",
}
search_engines = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "bing": "https://www.bing.com",
}


def open_url(url):
    webbrowser.open(url)
    chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
    webbrowser.get(chrome_path).open(url)


def search(search_query, search_engine):
    try:
        open_url(f"{search_engines[search_engine]}/search?q={search_query}")
    except IndexError:
        open_url(f"https://www.google.com/search?q={search_query}")


def speak(text):
    gui.speak(text)
    engine.say(text)
    engine.runAndWait()


def wish_me():
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
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    query = ""
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print("user said: " + query)

    except sr.UnknownValueError:
        print("Sorry Could You please try again")

    except Exception as e:
        print(e)
        print("Say That Again Please")

    return query


speak("Initializing Jarvis....")
wish_me()


def execute_the_command_said_by_user():
    query = take_command()

    # logic for executing basic tasks
    if "wikipedia" in query.lower():
        speak("Searching wikipedia....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif "what's up" in query or "how are you" in query:
        st_msgs = [
            "Just doing my thing!",
            "I am fine!",
            "Nice!",
            "I am nice and full of energy",
        ]
        speak(random.choice(st_msgs))

    elif "open" in query.lower():
        website = query.replace("open", "").strip().lower()
        try:
            open_url(popular_websites[website])
        except IndexError:  # If the website is unknown
            print(f"Unknown website: {website}")
            speak(f"Sorry, i don't know the website {website}")

    elif "search" in query.lower():
        search_query = query.split("for")[-1]
        search_engine = query.split("for")[0].replace("search", "").strip().lower()
        search(search_query, search_engine)

    elif "mail" in query:
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
        music_folder = "Your_music_folder_path(absolute_path)"
        music = ("music1", "music2", "music3", "music4")
        random_music = music_folder + random.choice(music) + ".mp3"
        speak("Playing your request")
        mixer.music.load(random_music)
        mixer.music.play()

    elif "pause music" in query:
        mixer.music.pause()

    elif "stop music" in query:
        mixer.music.stop()

    elif "unpause" in query:
        mixer.music.unpause()

    speak("Next Command! Sir!")


gui.set_speak_command(execute_the_command_said_by_user)
gui.mainloop()
