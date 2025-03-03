import os
import sys
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import subprocess

def download_mp3():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return
    
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_file = audio_stream.download(output_path="downloads")

        # Convert to MP3 using FFmpeg
        mp3_file = output_file.rsplit(".", 1)[0] + ".mp3"
        command = f'ffmpeg -i "{output_file}" -q:a 0 -map a "{mp3_file}" -y'
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        os.remove(output_file)  # Remove original file
        messagebox.showinfo("Success", f"Downloaded as: {mp3_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("SAR's YouTube to MP3 Converter")
root.geometry("400x200")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Convert to MP3", command=download_mp3)
download_button.pack(pady=20)

root.mainloop()
