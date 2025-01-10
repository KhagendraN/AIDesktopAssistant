
# AIDesktopAssistant

AIDesktopAssistant is a voice-enabled desktop assistant designed to interact with users through voice commands. It can perform various tasks like querying information, integrating with email, WhatsApp, and providing intelligent responses using AI.

## Features

- **Voice Interaction**: Capture user queries via voice input and provide vocal responses.
- **AI Classification**: Classifies user queries using a machine learning model (`classifier.pkl`).
- **Email & WhatsApp Integration**: Manage email and WhatsApp messages through voice commands.
- **Customizable Commands**: Extend the assistant with additional functionality as needed.
- **Simple Command Line Interface**: Start the assistant via a simple Python script.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Required Libraries

The project uses several libraries, including:

- `speech_recognition` for voice input
- `gTTS` for text-to-speech output
- `sklearn` for machine learning (SVC and TfidfVectorizer)
- `sounddevice` for audio recording
- `playsound` for audio playback

These will be installed automatically when you run the `pip install -r requirements.txt` command.

## Usage

### Running the Assistant

1. **Start the Assistant**: To begin using the voice assistant, run the following command:

    ```bash
    python app.py
    ```

2. **Voice Interaction**: The assistant will continuously listen for voice input and respond based on the query. Example queries might include:
    - "What is the capital of France?"
    - "Tell me a joke."
    - "Check my email."

### AI Classification

The assistant uses a machine learning classifier to understand and categorize different types of queries. The classifier is trained using a small set of data (stored in `training_data.json`). It can be extended to handle more sophisticated interactions as the project grows.

### Voice Input/Output

- **Voice Input**: The assistant listens for voice queries using the `speech_recognition` library.
- **Voice Output**: It uses `gTTS` to convert text responses to speech and plays them using `playsound`.

### Example Flow

1. **User**: "What is the capital of France?"
2. **Assistant**: "The capital of France is Paris."

## Code Explanation

### `app.py`

The main entry point to start the assistant. It listens for voice input, processes the query using a separate thread (via `dispatcher.py`), and then speaks the response.

```python
from dispatcher import dispatch_query
from voice import get_voice_input, speak
import threading
import queue

response_queue = queue.Queue()

def process_query(query):
    response = dispatch_query(query)
    response_queue.put(response)

def run_voice_interaction():
    while True:
        query = get_voice_input().lower()
        if query == "none":
            continue

        threading.Thread(target=process_query, args=(query,)).start()

        while True:
            try:
                response = response_queue.get(timeout=5)
                print(f"Assistant: {response}")
                speak(response)
                break
            except queue.Empty:
                continue

if __name__ == '__main__':
    run_voice_interaction()
```

### `classifier.py`

This script trains a text classifier using `TfidfVectorizer` and `SVC` from `sklearn` to classify user queries into categories like "friendly", "normal", and "long". The trained model and vectorizer are saved in `classifier.pkl` and `vectorizer.pkl`.

### `voice.py`

Handles voice input using the `speech_recognition` library and converts text responses to speech using `gTTS`.

```python
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening!")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}
")
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

def speak(text):
    if not text.strip():  # Check if text is empty
        print("No text to speak")
        return
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")
```

## Contributing

We welcome contributions! If you'd like to contribute, please fork the repository and create a pull request. Make sure your changes follow the code style and are well-documented.


