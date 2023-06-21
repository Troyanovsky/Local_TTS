# pip install TTS; Python version < 3.11
import tkinter as tk
from tkinter import filedialog
from TTS.api import TTS
from tkinter import messagebox
import os

class TTSApp:
    def __init__(self, master):
        self.master = master
        master.title("Text-to-Speech App")
        master.geometry("1280x720")
        self.default_output_folder = os.getcwd()  # Set default output folder to current working directory

        # Create text box for user input
        self.text_box = tk.Text(master, height=10, width=50)
        self.text_box.pack(fill=tk.BOTH, expand=True)

        # Create button to generate audio file
        self.generate_button = tk.Button(master, text="Generate", command=self.generate_audio)
        self.generate_button.pack()

        # Create button to choose output folder
        self.output_folder_button = tk.Button(master, text="Output Folder", command=self.choose_output_folder)
        self.output_folder_button.pack()

        # Create label to display selected output folder path
        self.output_folder_label = tk.Label(master, text="")
        self.output_folder_label.pack()

        # Initialize TTS object
        self.model_name = "tts_models/en/ljspeech/fast_pitch"
        self.vocoder_name = "vocoder_models/en/ljspeech/hifigan_v2"
        self.tts = TTS(self.model_name, vocoder_path=self.vocoder_name)

    def generate_audio(self):
        # Get user input from text box
        text = self.text_box.get("1.0", "end-1c")

        # Get output folder path from label
        output_folder_path = self.output_folder_label.cget("text")

        # Set output folder path to default if user does not choose a folder
        if not output_folder_path:
            output_folder_path = self.default_output_folder

        # Generate audio file from user input
        self.tts.tts_to_file(text=text, file_path=output_folder_path + "/output.wav")

        # Generate audio file from user input
        self.tts.tts_to_file(text=text, file_path=output_folder_path + "/output.wav")

        # Show message box when generation is done
        messagebox.showinfo("Generation Complete", "Audio file generated successfully!")

    def choose_output_folder(self):
        # Open file dialog to choose output folder
        output_folder_path = filedialog.askdirectory()

        # Set output folder path to default if user does not choose a folder
        if not output_folder_path:
            output_folder_path = self.default_output_folder

        # Update output folder label with selected folder path
        self.output_folder_label.config(text=output_folder_path)

root = tk.Tk()
app = TTSApp(root)
root.mainloop()