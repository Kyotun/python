import pygame
from pytube import YouTube
import requests
from tkinter import *

# Initialize pygame mixer

def download_and_play():
    try:
        youtube_audio_url = "https://www.youtube.com/watch?v=3slblDkOXw4&list=RD3slblDkOXw4&start_radio=1"
        
        print("1")
        # Get the stream URL for the audio
        response = requests.get(f"https://www.youtubeinmp3.com/fetch/?video={youtube_audio_url}")
        stream_url = response.json()["link"]
        print("2")

        # Download the audio
        audio_content = requests.get(stream_url).content
        with open('audio.mp3', 'wb') as audio_file:
            audio_file.write(audio_content)
        print("3")
            
        pygame.mixer.music.load('audio.mp3')
        pygame.mixer.music.play()
        print("4")

    except Exception as e:
        print("Error:", e)

# Create the main window
window = Tk()
window.title("YouTube Audio Player")

# Create a button to download and play the YouTube audio
play_button = Button(window, text="Download and Play", command=download_and_play)
play_button.pack()

# Run the GUI
window.mainloop()