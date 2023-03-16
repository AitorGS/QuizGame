from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

print(f"{question_bank} questions added")


quiz_brain = QuizBrain(question_bank)

while quiz_brain.has_more_questions():
    quiz_brain.next_question()

print(f"Quiz finished. Your score is {quiz_brain.score}")




# question1 = Question("Capital of Spain", "Madrid")
#
# print(question1.text)
# print(question1.answer)
