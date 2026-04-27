import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import pyaudio

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Take voice command
def take_command():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.WaitTimeoutError:
        speak("Listening timed out.")
        return None

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return None

    except sr.RequestError:
        speak("Network error.")
        return None

    except Exception as e:
        print("Error:", e)
        speak("Microphone error.")
        return None

# Respond function
def respond(command):
    if command is None:
        return

    # Greeting
    if 'hello' in command or 'hi' in command:
        speak("Hello! How can I help you?")

    # Time
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # Date
    elif 'date' in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

    # Search
    elif 'search' in command:
        speak("What should I search?")
        query = take_command()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    # Open websites
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif 'open whatsapp' in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")

    # Open apps (Windows)
    elif 'open chrome' in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif 'open calculator' in command:
        speak("Opening Calculator")
        os.system("start calc")

    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system("start notepad")

    # Exit
    elif 'exit' in command or 'quit' in command or 'bye' in command:
        speak("Goodbye! Have a great day.")
        sys.exit()

    # Unknown
    else:
        speak("I don't know that command.")

# Main loop
def run_assistant():
    speak("Hello, I am your assistant.")

    while True:
        command = take_command()
        respond(command)

# Run
if __name__ == "__main__":
    run_assistant()