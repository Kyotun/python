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

# Create a quizbrain object with question bank(question list)
quiz = QuizBrain(q_list=question_bank)
quiz_ui = QuizInterface()
quiz_ui.put_question(q_text=quiz.next_question())

# while quiz.still_has_question():
#     quiz.next_question()

# quiz.print_final_state()