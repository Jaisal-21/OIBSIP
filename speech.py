import speech_recognition as sr
import pyttsx3

def speak(text):
    print("Assistant:", text)

    try:
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)

        engine.say(str(text))
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print("Speech Error:", e)


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except Exception as e:
            print("Recognition Error:", e)
            return ""