import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
import os
import webbrowser

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Ask the user to select an audio file
audio_file_path = filedialog.askopenfilename(filetypes=[('Audio Files', '*.mp3 *.wav')])
audio_clip = AudioFileClip(audio_file_path)

# Ask the user to select one or more image files
image_files = filedialog.askopenfilenames(filetypes=[('Image Files', '*.png *.jpg *.jpeg')])

# Create a list of ImageClips from the selected image files
image_clips = [ImageClip(file).set_duration(audio_clip.duration) for file in image_files]

# Combine the ImageClips and the AudioClip into a single video clip
video_clip = concatenate_videoclips(image_clips)
video_clip = video_clip.set_audio(audio_clip)

# Ask the user to choose the output file location and name
output_file_path = filedialog.asksaveasfilename(defaultextension='.mp4', filetypes=[('MP4 files', '*.mp4')])

# Write the video clip to the output file
video_clip.write_videofile(output_file_path, fps=30, codec='libx264')

# Delete the audio and video clips to free up memory
del audio_clip
del image_clips
del video_clip

# Open the directory containing the output file
output_directory = os.path.dirname(output_file_path)
if os.name == 'nt': # Check if the OS is Windows
    os.startfile(output_directory)
else:
    webbrowser.open(output_directory)
