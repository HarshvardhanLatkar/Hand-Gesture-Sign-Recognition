import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import regex as re

class TextToImage:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Image")

        # Create a text entry widget
        self.label = ttk.Label(root, width=30)
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # Create a submit button
        self.submit_button = ttk.Button(root, text="Submit", command=self.link_text_to_image)
        self.submit_button.grid(row=0, column=1, padx=10, pady=10)

        self.exit_button = ttk.Button(root, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=0, column=2, padx=10, pady=10)

        # Create a label to display the linked image
        self.image_label = ttk.Label(root)
        self.image_label.grid(row=1, columnspan=2, padx=10, pady=10)

    def link_text_to_image(self, txt):
        # Get the text from the entry widget
        # text = self.entry.get()
        self.label.config(text=txt)
        pattern = r"[^\w\s]"  # Matches characters except alphanumeric and whitespace
        text = re.sub(pattern, "", txt).lower()

        image_mapping = {
            "dislike": "Dislike.png",
            "hello": "Hello.png",
            "like": "Like.png",
            "okay": "Okay.png",
            "peace": "Peace.png"
            # Add more mappings as needed
        }

        # Check if the entered text exists in image_mapping
        if text in image_mapping:
            image_path = f"Images\\{image_mapping[text]}"
            # Open the image using PIL
            img = Image.open(image_path)

            # Convert the image to Tkinter PhotoImage
            self.photo = ImageTk.PhotoImage(img)

            # Update the label with the linked image
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo
        else:
            # Display a message if no image found for the entered text
            self.image_label.config(text="No image found for the entered text: " + text)

# def main():
#     root = tk.Tk()
#     app = TextToImage(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
