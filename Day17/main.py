from QuestionModel import Question
from data import question_data
from quizbrain import QuizBrain

question_bank = []
for i in question_data:
    question_text = i["question"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    ans = quiz.next_question()

print("Quiz Completed!!!")
print(f"Your Score: {quiz.score}/{quiz.question_number}")