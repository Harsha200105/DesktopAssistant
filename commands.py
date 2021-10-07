import configparser
import random
import smtplib
import sys

import wikipedia
from pygame import mixer

from actions import open_url, search, speak

config = configparser.ConfigParser()  # if exists loads library.
config.read('config.ini')


def command_wikipedia(debug, query):
    speak("Searching wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    if debug == "True":
        print(results)
    else:
        pass
    speak(results)


def command_whatsup():
    stMsgs = [
        "Just doing my thing!",
        "I am fine!",
        "Nice!",
        "I am nice and full of energy",
    ]
    speak(random.choice(stMsgs))


def command_open(query, popular_websites, debug, search_engine, takeCommand):
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


def command_search(query, search_engine):
    search_query = query.split("for")[-1]
    search(search_query, search_engine)


def command_mail(takeCommand):
    speak("Who is the recipient? ")
    recipient = takeCommand()

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


def command_nothing():
    speak("okay")
    speak("Bye Sir, have a good day.")
    sys.exit()


def command_hello():
    speak("Hello Sir")


def command_bye():
    speak("Bye Sir, have a good day.")
    sys.exit()


def command_playMusic():
    try:
        music_folder = config['DEFAULT']['musicPath']
        music = ("music1", "music2", "music3", "music4")
        random_music = music_folder + random.choice(music) + ".mp3"
        speak("Playing your request")
        mixer.music.load(random_music)
        mixer.music.play()
    except Exception as e:
        speak(e)


def command_pauseMusic():
    mixer.music.pause()


def command_stopMusic():
    mixer.music.stop()


def command_unpauseMusic():
    mixer.music.unpause()
