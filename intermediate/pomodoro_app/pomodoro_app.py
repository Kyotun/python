from tkinter import *
import math
import os
import pygame
import time
import threading
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK_SEC = WORK_MIN * 60
SHORT_BREAK_MIN = 5
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_MIN = 20
LONG_BREAK_SEC = LONG_BREAK_MIN * 60
reps = 0
timer = None

# ---------------------------- MUSIC ------------------------------- #

playlist = ("intermediate/pomodoro_app/musics/experience.mp3",
            "intermediate/pomodoro_app/musics/foggy_today.mp3",
            "intermediate/pomodoro_app/musics/idea1.mp3",
            "intermediate/pomodoro_app/musics/idea22.mp3",
            "intermediate/pomodoro_app/musics/outsider_nomore.mp3",
            "intermediate/pomodoro_app/musics/see_you_tomorrow.mp3",
            "intermediate/pomodoro_app/musics/solas.mp3",
            "intermediate/pomodoro_app/musics/sonata.mp3",
            "intermediate/pomodoro_app/musics/table_for_two.mp3"
            )

currently_playing_song = playlist[0]
paused = False

def display_playlist(songs):
    for file_path in songs:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        playlist_box.insert(END, file_name)

def highlight_current_song(current_song):
    # Find the index of the currently playing song in the playlist
    index = playlist.index(current_song)
    
    # Highlight the currently playing song in the Listbox
    playlist_box.selection_clear(0, END)  # Clear previous selections
    playlist_box.selection_set(index)  # Select the currently playing song
    playlist_box.see(index)  # Ensure the selected item is visible in the Listbox
        
def stop_music():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True

def continue_music():
    global paused
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
        paused = False

def play_background_sound(songs):
    global currently_playing_song, paused
    pygame.init()
    pygame.mixer.init()
    for song in songs:
        currently_playing_song = song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
    
music_thread = threading.Thread(target=play_background_sound, args=(playlist,))
music_thread.start()

def go_forward():
    global currently_playing_song
    # Stop the current song
    pygame.mixer.music.stop()

    # Get the index of the current song in the playlist
    current_song_index = playlist.index(currently_playing_song)

    # Play the next song in the playlist
    next_song_index = (current_song_index + 1) % len(playlist)
    currently_playing_song = playlist[next_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    highlight_current_song(current_song=currently_playing_song)

def go_backward():
    global currently_playing_song
    # Stop the current song
    pygame.mixer.music.stop()

    # Get the index of the current song in the playlist
    current_song_index = playlist.index(currently_playing_song)

    # Play the previous song in the playlist
    prev_song_index = (current_song_index - 1) % len(playlist)
    currently_playing_song = playlist[prev_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    highlight_current_song(current_song=currently_playing_song)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    show_text.config(text="Timer", fg=GREEN, bg=YELLOW)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        show_text.config(text="It's time for a long break...", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        show_text.config(text="It's time for a 'kurze' Pause ;)", fg=PINK)
    else:
        count_down(WORK_SEC)
        show_text.config(text="Have a nice session!", fg=GREEN)
timer_thread = threading.Thread(target=start_timer)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
def count_down(count):
    min_left = math.floor(count / 60)
    second_left = count % 60
    if second_left < 10:
        second_left = f"0{second_left}"
        
    canvas.itemconfig(timer_text, text=f"{min_left}:{second_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App von Kyotun")
window.config(padx=100, pady=50, bg=YELLOW)

show_text = Label(text="Timer", font=(FONT_NAME, 50))
show_text.config(fg=GREEN, bg=YELLOW)
show_text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/kyotun/Desktop/python/intermediate/pomodoro_app/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
start_button = Button(width=1, text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(width=1, text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

forward_button = Button(width=6, text=f"Next Music", highlightbackground=YELLOW, command=go_forward)
forward_button.grid(row=2, column=6)

backward_button = Button(width=9, text=f"Previous Music", highlightbackground=YELLOW, command=go_backward)
backward_button.grid(row=2, column=3, padx=(70,0))

stop_button = Button(width=5, text="Stop Music", highlightbackground=YELLOW, command=stop_music)
stop_button.grid(row=2, column=4)

continue_button = Button(width=9, text="Continue Music", highlightbackground=YELLOW, command=continue_music)
continue_button.grid(row=2, column=5)

tik_symbol = Label(text="✔", font=("Roboto", 10))
tik_symbol.config(bg=YELLOW, fg=GREEN)
tik_symbol.grid(row=3, column=1)

playlist_box = Listbox(window, width=45)
playlist_box.grid(row=1, column=3, columnspan=4, padx=(70,0))

display_playlist(songs=playlist)
highlight_current_song(current_song=currently_playing_song)


window.mainloop()