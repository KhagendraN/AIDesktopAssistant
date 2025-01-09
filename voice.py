import sounddevice as sd
import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# Function to get voice input using sounddevice
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening!")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

# Function to convert text to speech and play it
def speak(text):
    if not text.strip():  # Check if text is empty
        print("No text to speak")
        return
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")
