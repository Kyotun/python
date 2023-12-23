from tkinter import *
import random
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

data = pd.read_csv("intermediate/flash_card_app/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}

def choose_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(data_dict)
    
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card, image=background_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
        
window = Tk()
window.title("Flashcard App von Kyotun")
window.config(width=900, height=626, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Images
background_image = PhotoImage(file="intermediate/flash_card_app/card_back.png")
front_image = PhotoImage(file="intermediate/flash_card_app/card_front.png")
right_image = PhotoImage(file="intermediate/flash_card_app/right.png")
wrong_image = PhotoImage(file="intermediate/flash_card_app/wrong.png")

# Canvases
canvas = Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(CARD_WIDTH/2, CARD_HEIGHT/2, image=front_image)
language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
word = canvas.create_text(400, 263, text="French Word", font=WORD_FONT, fill="black")
canvas.grid(row=0, column=0, columnspan=2)



# Buttons
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=choose_word)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=choose_word)
wrong_button.grid(row=1, column=0)

choose_word()

window.mainloop()
