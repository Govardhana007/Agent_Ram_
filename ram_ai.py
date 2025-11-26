import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initialize the AI "Ram"
engine = pyttsx3.init()
engine.setProperty('rate', 170)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ram is listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print(f"🧠 You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, service is down.")
        return ""


def run_ram():
    speak("Hi, I'm gopal. How can I help you?")
    command = listen()

    if "youtube" in command:
        speak("Opening YouTube")
        pywhatkit.playonyt("open YouTube")

    elif "search" in command:
        search_term = command.replace("search", "").strip()
        if search_term:
            speak(f"Searching Google for {search_term}")
            pywhatkit.search(search_term)
        else:
            speak("What do you want me to search?")

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time}")

    else:
        speak("Sorry, I can't do that yet.")


# Run the AI Ram
run_ram()
