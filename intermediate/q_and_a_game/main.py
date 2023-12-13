from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []
for question in question_data:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()
