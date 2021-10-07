import datetime
import webbrowser

import pyttsx3
import requests

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


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
