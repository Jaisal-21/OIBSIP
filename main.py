from speech import speak, listen
from commands import process_command
import commands as commands


speak(
    "Hello Jaisal. I am Vyra, your voice assistant. "
    "How can I help you?"
)

running = True

while running:

    if commands.sleep_mode:

        command = input(
            "Type wake up: "
        ).lower()

        if command == "wake up":

            commands.sleep_mode = False

            speak("I am awake and ready.")

        continue

    command = listen()

    if command:
        running = process_command(command)