import mediapipe as mp
import PIL.Image, PIL.ImageTk
from openai import OpenAI
import sounddevice as sd
import soundfile as sf
import numpy as np
from tkinter import *
import cv2
import tkinter as tk
import os


from TextToImage import TextToImage
def speech_to_sign():
    # sentence = simpledialog.askstring("Speech to Sign", "Enter the sentence you want to convert:")
    # if sentence:
    #     # Create a new window for displaying the converted sign language
    #     sign_window = tk.Toplevel(root)
    #     sign_window.title("Converted Sign Language")
    #
    #     # Dummy text, you can replace this with actual conversion logic
    #     sign_label = tk.Label(sign_window, text=f"Converted Sign Language for '{sentence}'")
    #     sign_label.pack()

    curItr = 0
    # while True:
    #     speech_to_wav(curItr)
    #     wav_to_text(curItr)
    #     if input("Would like to exit? (Y/N): ") in ["Y", "y"]:
    #         break

    # speech-to-text window
    master = Tk()
    master.geometry('500x350')
    master.title('Speech To Sign Language')
    frame = Frame(master, relief='sunken',
                  bd=1, bg='#20262E')
    # frame.place(x=0, y=0, anchor="nw", width=385, height=460)
    frame.pack(fill='both', expand=True, padx=50, pady=10)

    label = Label(frame, text='', width=100, height=0, fg="black")
    # label.config(text="")
    label.pack()
    # label.place(x=80, y=100)
    label.place(relx=0.5,
                rely=0.3,
                anchor='center')
    # Label.grid(row=5,column=4)

    button = tk.Button(frame, text='Record', width=8, height=1, font=("Arial", 16),fg="#F5EAEA" ,bg="#20262E",
                       command=lambda: speech_to_wav(label, curItr))
    button.pack()
    button.place(x=140, y=10)

    frame.mainloop()
    curItr += 1


def speech_to_wav(label, itr=0):
    # Define recording parameters
    duration = 5  # Recording duration in seconds
    fs = 44100  # Sampling rate

    # Record audio
    print("Start speaking...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    print("Recording stopped.")

    # Convert recorded audio to a NumPy array
    recording_array = myrecording.astype(np.float32)

    # Directly write the array to a WAV file using soundfile
    sf.write(f"{os.getcwd()}\\audio\\recording{itr}.wav", recording_array, fs)  # Replaces librosa.output.write_wav

    wav_to_text(label, itr)

def wav_to_text(label, itr=0):
    api_key = "API KEY"
    client = OpenAI(api_key=api_key)
    audio_file = open(f"{os.getcwd()}\\audio\\recording{itr}.wav", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="en"
    )
    txt = transcription.text
    label.config(text=txt)

    master = tk.Tk()
    tti = TextToImage(master)
    tti.link_text_to_image(txt)
    master.mainloop()

def main():
    speech_to_sign()

if __name__ == "__main__":
    main()
