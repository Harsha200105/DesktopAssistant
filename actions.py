import configparser
import datetime
import webbrowser

import pyttsx3
import requests


def search_engine_selector(config):
    if config['DEFAULT']['search_engine'] == 'Google':
        return "https://www.google.com"
    elif config['DEFAULT']['search_engine'] == 'Bing':
        return "https://www.bing.com"
    elif config['DEFAULT']['search_engine'] == 'DuckDuckGo':
        return "https://www.duckduckgo.com"
    elif config['DEFAULT']['search_engine'] == 'Youtube':
        return "https://www.youtube.com"
    else:
        # If none of default ones selected triesto fetch https://example.com
        # to see if its valid as search engine and if its valid it uses it.
        # If not valid it uses Google.
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


def wish_me(master):
    hour = datetime.datetime.now().hour
    # print(hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + master)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + master)

    else:
        speak("Good Evening" + master)

    # speak("Hey I am Jarvis. How may I help you")


def change_rate(query, take_command):
    try:
        rate = query.split('to')[-1]
        engine.setProperty('rate', int(rate))
        speak("¿Do you want to keep this config?")
        answer = take_command()
        if answer == "yes":
            config['DEFAULT']['rate'] = rate
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        else:
            pass
    except Exception:
        speak("Invalid value. Please try again.")


def change_voice(query, take_command):
    try:
        voice = query.split('to')[-1]
        if voice == "male":
            engine.setProperty('voice', voices[0].id)
            speak("¿Do you want to keep this config?")
            if take_command() == "yes":
                config['DEFAULT']['voice'] = 'Male'
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                pass

        elif voice == "female":
            engine.setProperty('voice', voices[1].id)
            speak("¿Do you want to keep this config?")
            answer = take_command()
            print(answer)
            if answer == "yes":
                config['DEFAULT']['voice'] = 'Female'
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                pass
        else:
            speak("Invalid value. Please try again.")
    except Exception:
        speak("Invalid value. Please try again.")


def change_volume(query, take_command):
    try:
        volume = query.split('to')[-1]
        engine.setProperty('volume', int(volume)/100)
        speak("¿Do you want to keep this config?")
        answer = take_command()
        if answer == "yes":
            config['DEFAULT']['volume'] = volume
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        else:
            pass
    except Exception:
        speak("Invalid value. Please try again.")


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

config = configparser.ConfigParser()
config.read('config.ini')

if config['DEFAULT']['voice'] == 'Male':
    engine.setProperty('voice', voices[0].id)
else:
    engine.setProperty('voice', voices[1].id)

try:
    engine.setProperty('rate', int(config['DEFAULT']['rate']))
    engine.setProperty('volume', int(config['DEFAULT']['volume'])/100)

except Exception:
    speak("Bad config. Setting up default values")
