class QuizBrain:
    """QuizBrain class evaluates the answers, ask questions and hold the score.
    """
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def print_final_state(self):
        print("Congrats, you've completed the quiz!")
        print(f"Your final score was: {self.score} out of {self.question_number}")

    def check_answer(self, user_input, correct_answer):
        """Answer and user input are boolean values.
        Check if user input equals to correct answer.
        If yes add score to 1 point.
        Print the correct answer and current score. 
        """
        if correct_answer.lower() == user_input.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Answer was wrong :/")
        print(f"Correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score} out of {self.question_number}")
        print("")

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_input=user_answer, correct_answer=current_question.answer)
