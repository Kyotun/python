from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import random
import random

question_bank = []
for question in question_data:
    """Take every question in question data dictionary and 
    save the questions and their answer to question bank.
    """
    question_text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=answer)
    question_bank.append(new_question)

# Create quizbrain and UI objects
quiz = QuizBrain(q_list=question_bank)
quiz_ui = QuizInterface(quizbrain=quiz)

