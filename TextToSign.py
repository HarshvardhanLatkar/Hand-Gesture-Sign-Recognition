import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TextToImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Image")

        # Create a text entry widget
        self.text_entry = ttk.Entry(root, width=30)
        self.text_entry.grid(row=0, column=0, padx=10, pady=10)

        # Create a submit button
        self.submit_button = ttk.Button(root, text="Submit", command=self.link_text_to_image)
        self.submit_button.grid(row=0, column=1, padx=10, pady=10)

        self.exit_button = ttk.Button(root, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=0, column=2, padx=10, pady=10)

        # Create a label to display the linked image
        self.image_label = ttk.Label(root)
        self.image_label.grid(row=1, columnspan=2, padx=10, pady=10)



    def link_text_to_image(self):
        # Get the text from the entry widget
        text = self.text_entry.get().lower()

        # Simple example: Map text to image file names
        image_mapping = {
            "dislike": "Dislike.jpg",
            "hello": "Hello.jpg",
            "like": "Like.jpg",
            "okay": "Okay.jpg",
            "peace": "peace.jpg",
            

            # Add more mappings as needed
        }

        # Check if the entered text exists in image_mapping
        if text in image_mapping:
            image_path = image_mapping[text]

            # Open the image using PIL
            img = Image.open(image_path)

            # Convert the image to Tkinter PhotoImage
            photo = ImageTk.PhotoImage(img)

            # Update the label with the linked image
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            # Display a message if no image found for the entered text
            self.image_label.config(text="No image found for the entered text: " + text)

def main():
    root = tk.Tk()
    app = TextToImageApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

