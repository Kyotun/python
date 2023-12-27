from tkinter import *
import random
import pandas as pd
import time

# Constants for to use
BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# Try to open saved not learned words. If there is.
# If the app is opened first time, there can't be.
try:
    data = pd.read_csv("intermediate/flash_card_app/words_to_learn.csv")
    print(len(data))
except FileNotFoundError:
    original_data = pd.read_csv("intermediate/flash_card_app/french_words.csv")
    print(len(original_data))
    learn_dict = original_data.to_dict(orient="records")
else:
    learn_dict = data.to_dict(orient="records")
current_card = {}

def known_word():
    """No parameter. Removes the current known card from the dictionary of the words to be learned.
    Saves the left words to be learned in csv format. Amount of words to be learned is decreased.
    Calls the new word function afterwards.
    """
    global current_card
    learn_dict.remove(current_card)
    words_to_learn_df = pd.DataFrame(learn_dict)
    words_to_learn_df.to_csv("intermediate/flash_card_app/words_to_learn.csv", index=False)
    new_word()
    
def new_word():
    """Selects a random card to be learned. Shows the new selected card in screen first in French.
    Calls the flip_card function at the end.
    """
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn_dict)
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    """Flips the card from French version of the words to English version.
    """
    canvas.itemconfig(card, image=background_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

# Create window and configure it with tkinter module functions.
window = Tk()
window.title("Flashcard App von Kyotun")
window.config(width=900, height=626, padx=50, pady=50, bg=BACKGROUND_COLOR)

# Wait 3 sec. to flip the card from french to english version.
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
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)

# Call the new_word function to trigger the functionality.
new_word()

window.mainloop()
