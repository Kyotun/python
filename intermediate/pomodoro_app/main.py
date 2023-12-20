from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
WORK_SEC = WORK_MIN * 60
SHORT_BREAK_MIN = 5
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_MIN = 20
LONG_BREAK_SEC = LONG_BREAK_MIN * 60
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps -= 1
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

start_button = Button(width=1, text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(width=1, text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

tik_symbol = Label(text="✔", font=("Roboto", 10))
tik_symbol.config(bg=YELLOW, fg=GREEN)
tik_symbol.grid(row=3, column=1)

window.mainloop()