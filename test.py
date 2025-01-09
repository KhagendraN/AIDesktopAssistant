from gtts import gTTS
import terminal

def speak(text):
    if not text.strip():  # Check if text is empty
        print("No text to speak")
        return
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")
    
speak("Hello sir, I'm samantha ")
