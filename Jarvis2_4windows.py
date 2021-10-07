import datetime
import random
import smtplib
import sys
import webbrowser
import pyttsx3
import wikipedia
import configparser
import os
import requests

import speech_recognition as sr

from pygame import mixer

mixer.init()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# this funcition checks which search engine is selected in config file.
def search_engine_selector():
    if config['DEFAULT']['search_engine'] == 'Google':
        return "https://www.google.com"
    elif config['DEFAULT']['search_engine'] == 'Bing':
        return "https://www.bing.com"
    elif config['DEFAULT']['search_engine'] == 'DuckDuckGo':
        return "https://www.duckduckgo.com"
    elif config['DEFAULT']['search_engine'] == 'Youtube':
        return "https://www.youtube.com"
    else:
        # If none of default ones selected
        try:
            if requests.get(
                f"https://{config['DEFAULT']['search_engine'].lower()}.com",
                params={'q': 'example'}
            ).status_code == 200:
                return (
                    f"https://{config['DEFAULT']['search_engine'].lower()}.com"
                )
            else:
                return "https://www.google.com"
        except Exception as e:
            print(e)
            return "https://www.google.com"


def open_url(url):
    webbrowser.open(url)
    chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
    webbrowser.get(chrome_path).open(url)


def search(search_query, search_engine):
    open_url(f"{search_engine}/search?q={search_query}")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe(MASTER):
    hour = datetime.datetime.now().hour
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    # speak("Hey I am Jarvis. How may I help you")


def main():
    MASTER = config['DEFAULT']['MASTER']

    popular_websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.org",
        "amazon": "https://www.amazon.com",
    }

    search_engine = search_engine_selector()

    debug = config['DEFAULT']['debug']

    if debug == "True":
        def takeCommand():
            query = input("Command |--> ")
            return query
    else:
        def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 0.5
                audio = r.listen(source)

            query = " "
            try:
                print("Recognizing....")
                query = r.recognize_google(audio, language="en-in")
                print("user said: " + query)

            except sr.UnknownValueError:
                if debug == "True":
                    print("Sorry Could You please try again")
                else:
                    pass
                speak("Sorry Could You please try again")

            except Exception as e:
                if debug == "True":
                    print(e)
                    print("Say That Again Please")
                else:
                    pass
                query = None

            return query

    speak("Initializing Jarvis....")
    wishMe(MASTER)
    while True:
        query = takeCommand()

        # logic for executing basic tasks
        if "wikipedia" in query.lower():
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            if debug == "True":
                print(results)
            else:
                pass
            speak(results)

        elif "what's up" in query or "how are you" in query:
            stMsgs = [
                "Just doing my thing!",
                "I am fine!",
                "Nice!",
                "I am nice and full of energy",
            ]
            speak(random.choice(stMsgs))

        elif "open" in query.lower():
            website = query.replace("open", "").strip().lower()
            try:
                open_url(popular_websites[website])
            except KeyError:  # If the website is unknown
                if debug == "True":
                    print(f"Unknown website: {website}")
                else:
                    pass
                speak(f"Sorry, i don't know the website {website}")
                speak(f"¿Do you want me to search {website} in the web?")
                if takeCommand() == "yes":
                    search(website, search_engine)
                else:
                    pass

        elif "search" in query.lower():
            search_query = query.split("for")[-1]
            search(search_query, search_engine)

        elif "mail" in query:
            speak("Who is the recipient? ")
            recipient = takeCommand()

            if "me" in recipient:
                try:
                    speak("What should I say? ")
                    content = takeCommand()

                    email = config['EMAIL']
                    server = smtplib.SMTP(email['server'], email['port'])
                    server.ehlo()
                    server.starttls()
                    server.login(email['username'], email['password'])
                    server.sendmail(email['username'], recipient, content)
                    server.close()
                    speak("Email sent!")
                except Exception:
                    speak("Sorry Sir!")
                    speak("I am unable to send your message at this moment!")

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
            try:
                music_folder = "Your_music_folder_path(absolute_path)"
                music = ("music1", "music2", "music3", "music4")
                random_music = music_folder + random.choice(music) + ".mp3"
                speak("Playing your request")
                mixer.music.load(random_music)
                mixer.music.play()
            except Exception as e:
                speak(e)

        elif "pause music" in query:
            mixer.music.pause()

        elif "stop music" in query:
            mixer.music.stop()

        elif "unpause" in query:
            mixer.music.unpause()

        speak("Next Command! Sir!")


if os.path.isfile('./config.ini'):  # Checks if config.ini exists.
    config = configparser.ConfigParser()  # if exists loads library.
    config.read('config.ini')  # and also the file.
    main()  # Then it launches the main program
else:
    # if it doesn't exist it drops an error message and exits.
    print('You need a config.ini file.')
    print('Check the documentation in the Github Repository.')
