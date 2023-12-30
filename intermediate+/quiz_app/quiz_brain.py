class QuizBrain:
    """QuizBrain class evaluates the answers, ask questions and hold the score.
    """
    def __init__(self, q_list):
        """
        Args:
            q_list (_List_): Contains Question objects as elements.
        """
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        self.current_question = None


    def check_answer(self, user_answer):
        """User answer is string type.
        Check if users answer equals to correct answer('True' or 'False').
        If yes add score to 1 point.
        Print the correct answer and current score. 
        """
        current_answer = self.current_question.answer
        if current_answer.lower() == user_answer.lower():
            self.score += 1
            return True
        else:
            return False


    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        """Takes the next question from question list.
        Asks user the answer.
        Compare the questions's answer and users answer.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q{self.question_number}: {self.current_question.text}"
