import os
import webbrowser
import pywhatkit
import re

from speech import speak
from utilities import tell_time, tell_date
from wikipedia_search import search_wikipedia
from reminders import set_reminder

sleep_mode = False


def process_command(command):

    global sleep_mode

    if "hello" in command:
        speak("Hello Jaisal. How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open calculator" in command:
        os.system("calc")
        speak("Opening Calculator")

    elif "search" in command:
        query = command.replace("search", "").strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        speak(f"Searching Google for {query}")

    elif "who is" in command or "what is" in command:

        query = command.replace("who is", "")
        query = query.replace("what is", "")
        query = query.strip()

        speak("Searching Wikipedia")

        result = search_wikipedia(query)

        speak(result.split(".")[0])

    elif "play" in command:

        song = command.lower()

        remove_words = [
            "can you",
            "please",
            "play",
            "song",
            "on youtube",
            "assistant"
        ]

        for word in remove_words:
            song = song.replace(word, "")

        song = song.strip()

        if song:

            speak(f"Playing {song}")

            pywhatkit.playonyt(song)

            sleep_mode = True

            speak("Entering sleep mode")

    elif "remind me to" in command and "in" in command:

        match = re.search(
            r"remind me to (.*?) in (\d+) minute",
            command
        )

        if match:

            task = match.group(1)
            minutes = int(match.group(2))

            set_reminder(task, minutes)

            speak(
                f"I will remind you to {task} in {minutes} minutes."
            )

    elif "who are you" in command:

        speak(
            "Hello! I am Vyra, an AI-powered voice assistant. I can answer questions, perform tasks, open applications, search for information, and help you interact with your device using natural voice commands."
        )

    elif "what can you do" in command:

        speak(
            "I can tell time and date, search Google, "
            "search Wikipedia, play songs, open websites, "
            "set reminders and more."
        )

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False

    else:
        speak("I don't know that command yet.")

    return True