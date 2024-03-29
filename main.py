import tkinter as tk
from gtts import gTTS
from tempfile import TemporaryFile
import pygame
from tkinter import filedialog
import webbrowser

def process_input():
    text = text_input.get("1.0", "end-1c")
    tts = gTTS(text=text, lang='en')
    temp_file = TemporaryFile()
    tts.write_to_fp(temp_file)
    temp_file.seek(0)
    output_label.config(text="Audio generated for input text")
    listen_button.config(state=tk.NORMAL, command=lambda: listen_audio(temp_file))
    download_button.config(state=tk.NORMAL, command=lambda: download_audio(temp_file))

def listen_audio(temp_file):
    temp_file.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

def download_audio(temp_file):
    temp_file.seek(0)
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")])
    if save_path:
        with open(save_path, "wb") as f:
            f.write(temp_file.read())
        output_label.config(text=f"Audio downloaded as {save_path}")

def open_link(event):
    webbrowser.open("https://www.youtube.com/c/SAMEERSHRINATH/null")

# Create the main window
root = tk.Tk()
root.title("Awaz app")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to 40% of the screen size
window_width = int(screen_width * 0.4)
window_height = int(screen_height * 0.4)
root.geometry(f"{window_width}x{window_height}")

# Create a label and text widget for text input
tk.Label(root, text="Enter your text:").pack()
text_input = tk.Text(root, height=5, wrap="word")
text_input.pack(padx=10, pady=5)  # Add padx and pady for left and right margins

# Create a button to submit the input
submit_button = tk.Button(root, text="Convert to Voice", command=process_input)
submit_button.pack()

# Create a label to display the output
output_label = tk.Label(root, text="")
output_label.pack()

# Create a button to listen to the audio
listen_button = tk.Button(root, text="Listen Audio", state=tk.DISABLED)
listen_button.pack()

# Create a button to download the audio
download_button = tk.Button(root, text="Download Audio", state=tk.DISABLED)
download_button.pack()

# Create the developer label
developer_label = tk.Label(root, text="Developer Sameer Shrinath", cursor="hand2", fg="black", font=("Arial", 10, "italic", "underline"))
developer_label.pack(side="bottom", pady=10)

# Bind events to the developer label
developer_label.bind("<Enter>", lambda e: developer_label.config(fg="blue"))
developer_label.bind("<Leave>", lambda e: developer_label.config(fg="black"))
developer_label.bind("<Button-1>", open_link)

# Run the Tkinter event loop
root.mainloop()
