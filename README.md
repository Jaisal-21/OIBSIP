# 🎙️ Vyra - Voice Assistant

Vyra is a Python-based Voice Assistant developed as part of the Oasis Infobyte Internship Program (OIBSIP).

The assistant can recognize voice commands, respond using speech synthesis, search Wikipedia, play songs on YouTube, open websites, tell the current date and time, and set reminders.

---

## 🚀 Features

- 🎤 Voice Command Recognition
- 🔊 Text-to-Speech Responses
- 🕒 Tell Current Time
- 📅 Tell Current Date
- 🌐 Open Google
- ▶️ Open YouTube
- 🔍 Google Search
- 📚 Wikipedia Search
- 🎵 Play Songs on YouTube
- ⏰ Reminder System
- 😴 Sleep Mode
- 🤖 Assistant Introduction & Help Commands

---

## 🛠️ Technologies Used

- Python 3.11
- SpeechRecognition
- pyttsx3
- Requests
- PyWhatKit
- Plyer
- Threading
- Datetime
- Webbrowser

---

## 📂 Project Structure

```text
voice_assist/
│
├── main.py
├── commands.py
├── speech.py
├── utilities.py
├── wikipedia_search.py
├── reminders.py
│
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Jaisal-21/OIBSIP.git
```

### Move into Project Folder

```bash
cd OIBSIP
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install pywhatkit
pip install plyer
pip install pyaudio
```

---

## ▶️ Run Project

```bash
python main.py
```

---

## 🎤 Available Voice Commands

### Greetings

```text
hello
```

### Date & Time

```text
what is the time
tell me the date
```

### Google

```text
open google
search python programming
```

### YouTube

```text
open youtube
play pasoori
play shape of you
```

### Wikipedia Search

```text
who is APJ Abdul Kalam
what is Python
```

### Reminders

```text
remind me to study python in 2 minute
```

### Assistant Information

```text
who are you
what can you do
```

### Sleep Mode

```text
play song
```

Assistant enters sleep mode while the song is playing.

Wake Up:

```text
wake up
```

### Exit

```text
stop
exit
```

---

## 🏗️ Project Architecture

```text
User Voice
     │
     ▼
Speech Recognition
     │
     ▼
Command Processing
     │
 ┌───┼───────────────┐
 │   │               │
 ▼   ▼               ▼
Time Wikipedia   Google Search
 │       │            │
 ▼       ▼            ▼
Reminder  Music   Applications
     │
     ▼
Text To Speech
     │
     ▼
Voice Response
```

---

## 📸 Sample Output

```text
You: who is APJ Abdul Kalam

Assistant: Searching Wikipedia

Assistant: A. P. J. Abdul Kalam was an Indian aerospace scientist and statesman...
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Speech Recognition
- Text-to-Speech Conversion
- API Integration
- Wikipedia Data Retrieval
- Multithreading
- Desktop Notifications
- Python Modular Programming
- Error Handling
- Voice-Based User Interaction

---

## 📜 Internship Details

**Organization:** Oasis Infobyte

**Internship Domain:** Python Programming

**Project Title:** Voice Assistant (Vyra)

**Intern:** S. Jaisal

---

## 📄 License

This project is developed for educational and internship purposes.