# Simple-Personal-Assistant-using-Python-speech-libraries
Here’s a clean, professional **README.md file** for your Voice Assistant project 👇

---

# 🎙️ Voice Assistant in Python

A simple Voice Assistant built using Python that can recognize voice commands and perform tasks like searching the web, opening applications, and telling time/date.

---

## 🚀 Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech responses
* 🌐 Google search via voice
* ▶️ Open YouTube, Google, WhatsApp Web
* 🖥️ Open system apps (Chrome, Calculator, Notepad)
* ⏰ Tell current time and date
* ❌ Exit on command

---

## 🛠️ Technologies Used

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Webbrowser
* OS module

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

---

### 2. Install dependencies

```bash
pip install SpeechRecognition pyttsx3
pip install pipwin
pipwin install pyaudio
```

---

### ⚠️ Important Note (PyAudio Issue)

If you face error:

```
ModuleNotFoundError: No module named 'pyaudio'
```

👉 This usually happens on newer Python versions.

### ✅ Solution:

* Use **Python 3.8 – 3.10**
* Or install PyAudio using:

```bash
python -m pipwin install pyaudio
```

---

## ▶️ How to Run

```bash
python assistant.py
```

---

## 🎤 Example Commands

* "Hello"
* "What is the time"
* "Search Python tutorials"
* "Open YouTube"
* "Open Google"
* "Open WhatsApp"
* "Open Calculator"
* "Exit"

---

## ⚠️ Requirements

* Working microphone 🎤
* Internet connection 🌐 (for speech recognition)

---

## 🧪 Troubleshooting

### ❌ Microphone not working

* Check system microphone settings
* Allow microphone permissions

### ❌ Speech not recognized

* Ensure stable internet connection

### ❌ PyAudio installation error

* Install using `pipwin`
* Use compatible Python version

---

## 🔥 Future Improvements

* 🤖 Integration with AI (ChatGPT)
* 🎵 Play music via voice
* 📩 Send WhatsApp messages
* 🖥️ GUI-based assistant
* 🌍 Multi-language support

---

## 👨‍💻 Author

**Muhammad Suffiyan Rafi**
Computer Scientist | AI/ML Enthusiast

---

