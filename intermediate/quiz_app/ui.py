from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WIDTH = 600
HEIGHT = 600
WIDTH_CANVAS = 300
HEIGTH_CANVAS = 250
FONT = ("Arial", 20, "italic")

class QuizInterface:
    
    def __init__(self, quizbrain: QuizBrain):
        self.q_brain = quizbrain
        self.window = Tk()
        self.window.title("Quiz App von Kyotun")
        self.window.config(width=WIDTH, height=HEIGHT, padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text=f"Score: {self.q_brain.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.true_image = PhotoImage(file="intermediate/quiz_app/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)
        
        self.wrong_image = PhotoImage(file="intermediate/quiz_app/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.click_false)
        self.wrong_button.grid(row=2, column=1)
        
        self.quote_canvas = Canvas(width=WIDTH_CANVAS, height=HEIGTH_CANVAS, bg="white")
        self.quote_canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.quote = self.quote_canvas.create_text(WIDTH_CANVAS/2, HEIGTH_CANVAS/2, widt=WIDTH_CANVAS-20, text="ASD", font=FONT, fill=THEME_COLOR)
        
        self.put_question()
        
        self.window.mainloop()
        
        
    def put_question(self):
        """Turns canvas into white after user answer.
        If there is still questions, scoreboard will be updated and next question will be shown in canvas.
        Otherwise, buttons will be disabled and text of canvas will be changed.
        """
        self.quote_canvas.config(bg="white")
        if self.q_brain.still_has_question():
            self.score_label.config(text=f"Score: {self.q_brain.score}")
            q_text = self.q_brain.next_question()
            self.quote_canvas.itemconfig(self.quote, text=q_text)
        else:
            self.quote_canvas.itemconfig(self.quote, text="There is no more question left!")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    
    
    def click_true(self):
        self.give_feedback(self.q_brain.check_answer("True"))
    
    
    def click_false(self):
        self.give_feedback(self.q_brain.check_answer("False"))
        
    
    def give_feedback(self, is_right):
        """Turns the canvas into red if user could not know the answer. Otherwise, into green.
        
        Args:
            is_right (bool): True if user was right.
        """
        if is_right:
            self.quote_canvas.config(bg="green")
        else:
            self.quote_canvas.config(bg="red")
        self.window.after(1000, self.put_question)