import tkinter as tk
from tkinter import messagebox, simpledialog
import cv2
import os
import PIL.Image, PIL.ImageTk

# Define root globally
root = None

#def run_program():
            #os.system('testgui.py')

def on_enter(event):
    event.widget.config(relief=tk.RAISED, borderwidth=5)

def on_leave(event):
    event.widget.config(relief=tk.FLAT, borderwidth=1)

def text_to_sign():
    os.system('TextToSign.py')




def speech_to_text():
    os.system("SpeechToText.py")



    

def main():
    # Define root as a global variable
    global root
    # Create the main window
    root = tk.Tk()
    root.title("Sign Language Converter")

    # Set the initial window size and background color
    root.geometry("1100x600")
    root.configure(bg="#363636")  # Light gray background color

    # Create a label with some styling
    label = tk.Label(root, text="Speech to Sign", font=('Comic Sans MS', 60, "bold"),fg="#F5EAEA", bg="#363636")
    label.pack(pady=(50, 20))  # Add more space between label and buttons

    # Create a frame to hold the buttons vertically centered
    button_frame = tk.Frame(root, bg='#222021')
    button_frame.pack()

    # Create a button for Sign to Speech with styling
    sign_to_speech_button = tk.Button(button_frame, text="Speech to Text", command=speech_to_text,
                                      font=("Calisto MT", 25, "bold") ,fg="#F5EAEA", bg="#20262E", width=30, height=3)
    sign_to_speech_button.pack(side=tk.TOP, padx=10, pady=10)
    sign_to_speech_button.bind("<Enter>", on_enter)
    sign_to_speech_button.bind("<Leave>", on_leave)

    # Create a button for Speech to Sign with styling
    speech_to_sign_button = tk.Button(button_frame, text="Text to Sign language", command=text_to_sign,
                                      font=("Calisto MT", 25, "bold"), fg="#F5EAEA", bg="#20262E", width=30, height=3)
    speech_to_sign_button.pack(side=tk.TOP, padx=10, pady=10)
    speech_to_sign_button.bind("<Enter>", on_enter)
    speech_to_sign_button.bind("<Leave>", on_leave)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
