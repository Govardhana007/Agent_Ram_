Ram — Simple Voice Assistant (Python)

A lightweight, beginner-friendly voice assistant written in Python. It listens to your voice, recognizes simple commands, speaks back responses, and can open YouTube, perform Google searches, and tell the current time.

Note: The assistant is referred to as Ram in the project, but the current code says "Hi, I'm gopal." on startup. You may want to change that to keep the name consistent.

Features

Voice input using your microphone

Speech-to-text via Google Web Speech API (speech_recognition)

Text-to-speech using pyttsx3

Play YouTube videos and run Google searches with pywhatkit

Tell the current local time

Simple, easy-to-extend command structure

Files

ram_assistant.py — main Python script (your provided code)

requirements.txt — dependencies (example below)

README.md — this file

Requirements

Python 3.8+

A working microphone and speakers

Internet connection (for speech_recognition Google recognizer & pywhatkit functionality)

OS-level microphone permissions (grant access on Windows/Mac/Linux desktop environment)

Example requirements.txt:

SpeechRecognition
pyttsx3
pywhatkit
pyaudio   # or an alternative wheel for your OS


Note about PyAudio: Installing pyaudio can be tricky on some platforms. On Windows you may install from a prebuilt wheel (e.g., pip install pipwin then pipwin install pyaudio) or use system-specific instructions for macOS/Linux.

Installation

Clone the repo:

git clone https://github.com/yourusername/ram-voice-assistant.git
cd ram-voice-assistant


(Optional) Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


If you don't have requirements.txt, install manually:

pip install SpeechRecognition pyttsx3 pywhatkit pyaudio

Usage

Run the assistant:

python ram_assistant.py


On start, Ram will say a greeting and listen for commands. Speak clearly.

Supported commands (as implemented)

Say something containing "youtube" — opens YouTube (via pywhatkit.playonyt)

Say something containing "search <term>" — performs a Google search for \<term\>

Say "time" — Ram speaks the current time

Any unsupported command returns: "Sorry, I can't do that yet."

Example voice phrases:

"Open YouTube"

"Search latest football scores"

"What's the time"

"Tell me the time"

Example code (improvements you might want)

To keep the assistant name consistent, change the greet line:

speak("Hi, I'm Ram. How can I help you?")

Common issues & troubleshooting

No audio input / microphone not detected

Make sure your microphone is connected and selected as the default recording device.

Grant microphone access to Python/terminal/IDE.

On Windows, check Privacy > Microphone settings.

pyaudio installation errors

Use prebuilt wheels or pipwin on Windows:

pip install pipwin
pipwin install pyaudio


On macOS, you may need: brew install portaudio then pip install pyaudio.

On Linux: install system packages (e.g., sudo apt-get install portaudio19-dev python3-pyaudio) then pip install pyaudio.

speech_recognition giving RequestError

This uses the Google Web Speech API which requires an internet connection.

If you want offline recognition, consider using other engines (e.g., Vosk).

Speech is choppy / too fast or too slow

Adjust TTS rate:

engine.setProperty('rate', 170)  # lower = slower, higher = faster

Extending Ram

Ideas to extend functionality:

Add more commands (weather, reminders, open local apps)

Use if-elif or command mapping with functions for cleaner code

Add hotword detection so Ram listens only on a wake word

Use offline speech recognition (Vosk) or other TTS engines

Add logging and error handling for robustness

Contributing

Contributions welcome! Feel free to open issues or pull requests. For major changes, open an issue first to discuss what you’d like to change.

License

Choose a license for your project (e.g., MIT). Example:

MIT License

Acknowledgements

SpeechRecognition by Uberi

pyttsx3 for offline TTS

pywhatkit for YouTube & Google search helpers

Ready-to-copy README

Below is the full README in one block ready to paste into your README.md:

# Ram — Simple Voice Assistant (Python)

A lightweight, beginner-friendly voice assistant written in Python. It listens to your voice, recognizes simple commands, speaks back responses, and can open YouTube, perform Google searches, and tell the current time.

> **Note:** The assistant is referred to as **Ram** in the project, but the current code says "Hi, I'm gopal." on startup. You may want to change that to keep the name consistent.

---

## Features
- Voice input using your microphone
- Speech-to-text via Google Web Speech API (`speech_recognition`)
- Text-to-speech using `pyttsx3`
- Play YouTube videos and run Google searches with `pywhatkit`
- Tell the current local time
- Simple, easy-to-extend command structure

---

## Files
- `ram_assistant.py` — main Python script (your provided code)
- `requirements.txt` — dependencies (example below)
- `README.md` — this file

---

## Requirements
- Python 3.8+
- A working microphone and speakers
- Internet connection (for `speech_recognition` Google recognizer & `pywhatkit` functionality)
- OS-level microphone permissions (grant access on Windows/Mac/Linux desktop environment)

Example `requirements.txt`:


SpeechRecognition
pyttsx3
pywhatkit
pyaudio # or an alternative wheel for your OS


> **Note about PyAudio:** Installing `pyaudio` can be tricky on some platforms. On Windows you may install from a prebuilt wheel (e.g., `pip install pipwin` then `pipwin install pyaudio`) or use system-specific instructions for macOS/Linux.

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/yourusername/ram-voice-assistant.git
cd ram-voice-assistant


(Optional) Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


If you don't have requirements.txt, install manually:

pip install SpeechRecognition pyttsx3 pywhatkit pyaudio

Usage

Run the assistant:

python ram_assistant.py


On start, Ram will say a greeting and listen for commands. Speak clearly.

Supported commands (as implemented)

Say something containing "youtube" — opens YouTube (via pywhatkit.playonyt)

Say something containing "search <term>" — performs a Google search for <term>

Say "time" — Ram speaks the current time

Any unsupported command returns: "Sorry, I can't do that yet."

Example voice phrases:

"Open YouTube"

"Search latest football scores"

"What's the time"

"Tell me the time"

Example code (improvements you might want)

To keep the assistant name consistent, change the greet line:

speak("Hi, I'm Ram. How can I help you?")

Common issues & troubleshooting

No audio input / microphone not detected

Make sure your microphone is connected and selected as the default recording device.

Grant microphone access to Python/terminal/IDE.

On Windows, check Privacy > Microphone settings.

pyaudio installation errors

Use prebuilt wheels or pipwin on Windows:

pip install pipwin
pipwin install pyaudio


On macOS, you may need: brew install portaudio then pip install pyaudio.

On Linux: install system packages (e.g., sudo apt-get install portaudio19-dev python3-pyaudio) then pip install pyaudio.

speech_recognition giving RequestError

This uses the Google Web Speech API which requires an internet connection.

If you want offline recognition, consider using other engines (e.g., Vosk).

Speech is choppy / too fast or too slow

Adjust TTS rate:

engine.setProperty('rate', 170)  # lower = slower, higher = faster

Extending Ram

Ideas to extend functionality:

Add more commands (weather, reminders, open local apps)

Use if-elif or command mapping with functions for cleaner code

Add hotword detection so Ram listens only on a wake word

Use offline speech recognition (Vosk) or other TTS engines

Add logging and error handling for robustness

Contributing

Contributions welcome! Feel free to open issues or pull requests. For major changes, open an issue first to discuss what you’d like to change.

License

Choose a license for your project (e.g., MIT). Example:

MIT License

Acknowledgements

SpeechRecognition by Uberi

pyttsx3 for offline TTS

pywhatkit for YouTube & Google search helpers


---


