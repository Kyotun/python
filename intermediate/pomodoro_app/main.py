from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App von Kyotun")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 50))
timer.config(fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/kyotun/Desktop/python/intermediate/pomodoro_app/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(width=1, text="Start", highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(width=1, text="Reset", highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

tik_symbol = Label(text="✔", font=("Roboto", 10))
tik_symbol.config(bg=YELLOW, fg=GREEN)
tik_symbol.grid(row=3, column=1)

window.mainloop()