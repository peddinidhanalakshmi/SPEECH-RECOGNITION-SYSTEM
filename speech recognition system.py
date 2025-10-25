# Speech Recognition using SpeechRecognition library

import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load an audio file (example.wav should be a short spoken sentence)
audio_file = "sample_audio.wav"

# Read the audio file
with sr.AudioFile(audio_file) as source:
    print("Listening to the audio...")
    audio_data = recognizer.record(source)
    print("Recognizing...")

    # Convert speech to text
    text = recognizer.recognize_google(audio_data)
    print("\nTranscribed Text:")
    print(text)