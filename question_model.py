class Question:
    """Models a question object with its text and its valid answer"""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return self.text + " " + self.answer




