from tkinter import *

THEME_COLOR = "#375362"
WIDTH = 600
HEIGHT = 600
WIDTH_CANVAS = 300
HEIGTH_CANVAS = 250
FONT = ("Arial", 20, "italic")

class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App von Kyotun")
        self.window.config(width=WIDTH, height=HEIGHT, padx=20, pady=20, bg=THEME_COLOR)
        
        self.right_image = PhotoImage(file="intermediate/quiz_app/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0)
        self.right_button.grid(row=2, column=0)
        
        self.wrong_image = PhotoImage(file="intermediate/quiz_app/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)
        
        self.quote_canvas = Canvas(width=WIDTH_CANVAS, height=HEIGTH_CANVAS, bg="white")
        self.quote_canvas.grid(row=1, column=0, columnspan=2)
        self.quote = self.quote_canvas.create_text(WIDTH_CANVAS/2, HEIGTH_CANVAS/2, text="ASD", font=FONT, fill="black")
        
        self.window.mainloop()
        
    def put_question(self, q_text):
        self.quote_canvas.itemconfig(self.quote, text=q_text)