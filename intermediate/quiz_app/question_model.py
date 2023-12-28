import html

class Question:
    """Question object will have the attributes answer and text(question)
    """
    def __init__(self, q_text, q_answer):
        self.answer = q_answer
        self.text = html.unescape(q_text)

