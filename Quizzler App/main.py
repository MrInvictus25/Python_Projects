from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    #print(question_bank[0].text)
    #print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
quizUI = QuizInterface(quiz) # I will need to extract questions from the data and embedd it tkinter GUI

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
