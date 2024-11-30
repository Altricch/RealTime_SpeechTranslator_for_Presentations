import sounddevice as sd
import numpy as np
import speech_recognition as sr
from transformers import pipeline
import io
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import Text
from threading import Thread

# Initialize the translator pipeline from Hugging Face
# TODO: make dict to include multiple model cards
translator = pipeline("translation_en_to_it", model="Helsinki-NLP/opus-mt-en-it")

# Function to record audio
# TODO: Multithread audio and input into a queue to be separately processed. Optimise for CPU
def record_audio():
    fs = 16000  # Sample rate (16 kHz)
    duration = 5  # seconds
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    return audio, fs

# Function to convert the audio to text and translate
def recognize_and_translate():
    recognizer = sr.Recognizer()
    while True:
        try:
            # Capture audio using sounddevice (from inbuilt microphone)
            audio, fs = record_audio()

            # Convert the numpy array to a byte-like object (WAV format)
            byte_io = io.BytesIO()
            write(byte_io, fs, audio)  
            byte_io.seek(0)  

            # Create an AudioData object
            audio_data = sr.AudioData(byte_io.read(), fs, 2)  

            # Convert audio into recognizable text
            text = recognizer.recognize_google(audio_data, language="en-US")

            # Translate the recognized text
            translation = translator(text)
            translated_text = translation[0]['translation_text']
            
            # Update the UI with the translated text
            update_ui(translated_text)
        
        except sr.UnknownValueError:
            continue  # Ignore unknown value errors and continue with the loop
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Function to update the text in the Tkinter UI
def update_ui(translated_text):
    
    text_area.delete(1.0, tk.END)  
    text_area.insert(tk.END, translated_text)
    text_area.tag_configure("center", justify='center')
    text_area.tag_add("center", 1.0, tk.END) 

    text_area.yview(tk.END)  

# Function to run the speech recognition and translation in a separate thread
def run_in_thread():
    # Run the speech recognition and translation in a separate thread
    translation_thread = Thread(target=recognize_and_translate, daemon=True)
    translation_thread.start()

# Set up the Tkinter window (UI)
root = tk.Tk()
root.title("Real-Time Translation (English to Italian)")

# Ensure the window stays on top of others
root.attributes("-topmost", True)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window width to the screen width and a fixed height (say 10% of the screen height)
window_width = screen_width
window_height = int(screen_height * 0.1)  # Adjust this percentage for more or less height

# Set the window geometry
root.geometry(f"{window_width}x{window_height}")

# Set up the Text widget (not ScrolledText)
text_area = Text(root, wrap=tk.WORD, font=("Helvetica", 32), bg="black", fg="white", bd=0, highlightthickness=0)
text_area.config(width=0, height=3)  # No borders, fixed height, will expand horizontally

# Set the Text widget to fill the entire window width and height
text_area.place(relwidth=1.0, relheight=1.0)  # Full width and height

# Set up the window properties
root.configure(bg="black")  # Set the background color to black

# Ensure topmost stays on during runtime
def ensure_on_top():
    root.attributes("-topmost", True)
    root.after(1000, ensure_on_top)  # Reapply every second to ensure it stays on top

ensure_on_top()

# Start the real-time translation process
run_in_thread()

# Start the Tkinter event loop
root.mainloop()
