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
    command_pause_music,
    command_play_music,
    command_search,
    command_stop_music,
    command_unpause_music,
    command_whatsup,
    command_wikipedia,
)

popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "GitHub": "https://www.github.com",
}


def main(search_engine, takeCommand, debug):
    while True:
        query = takeCommand().lower()

        # logic for executing commands without arguments
        phrases = {
            "what's up": command_whatsup,
            "nothing": command_nothing,
            "abort": command_nothing,
            "stop": command_nothing,
            "hello": command_hello,
            "bye": command_bye,
            "play music": command_play_music,
            "unpause": command_unpause_music,
            "pause music": command_pause_music,
            "stop music": command_stop_music,
        }
        for phrase, command in phrases.items():
            if phrase in query:
                command()

        # logic for executing commands with arguments
        if "wikipedia" in query.lower():
            command_wikipedia(speak, debug, query)

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

        speak("Next Command! Sir!")


def run():
    master = config['DEFAULT']['master']

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
    wishMe(master)
    main(search_engine, takeCommand, debug)


if os.path.isfile('./config.ini'):  # Checks if config.ini exists.
    config = configparser.ConfigParser()  # if exists loads library.
    config.read('config.ini')  # and also the file.
    run()  # Then it launches the main program
else:
    # if it doesn't exist it drops an error message and exits.
    print('You need a config.ini file.')
    print('Check the documentation in the Github Repository.')
