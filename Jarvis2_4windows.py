import configparser
import os

import speech_recognition as sr

from actions import search_engine_selector, speak, wishMe
from commands import (
    command_bye,
    command_hello,
    command_mail,
    command_nothing,
    command_open,
    command_pauseMusic,
    command_playMusic,
    command_search,
    command_stopMusic,
    command_unpauseMusic,
    command_whatsup,
    command_wikipedia,
)

popular_websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.org",
        "amazon": "https://www.amazon.com",
    }


def main(search_engine, takeCommand, debug):
    while True:
        query = takeCommand()

        # logic for executing basic tasks
        if "wikipedia" in query.lower():
            command_wikipedia(speak, debug, query)

        elif "what's up" in query or "how are you" in query:
            command_whatsup()

        elif "open" in query.lower():
            command_open(
                query,
                popular_websites,
                debug,
                search_engine,
                takeCommand
            )

        elif "search" in query.lower():
            command_search(query, search_engine)

        elif "mail" in query:
            command_mail(takeCommand)

        elif "nothing" in query or "abort" in query or "stop" in query:
            command_nothing()

        elif "hello" in query:
            command_hello()

        elif "bye" in query:
            command_bye()

        elif "play music" in query:
            command_playMusic()

        elif "pause music" in query:
            command_pauseMusic()

        elif "stop music" in query:
            command_stopMusic()

        elif "unpause" in query:
            command_unpauseMusic()

        speak("Next Command! Sir!")


def run():
    MASTER = config['DEFAULT']['MASTER']

    search_engine = search_engine_selector(config)

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

    speak(text="Initializing Jarvis....")
    wishMe(MASTER)
    main(search_engine, takeCommand, debug)


if os.path.isfile('./config.ini'):  # Checks if config.ini exists.
    config = configparser.ConfigParser()  # if exists loads library.
    config.read('config.ini')  # and also the file.
    run()  # Then it launches the main program
else:
    # if it doesn't exist it drops an error message and exits.
    print('You need a config.ini file.')
    print('Check the documentation in the Github Repository.')
