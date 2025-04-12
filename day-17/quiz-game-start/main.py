from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# for item in question_bank:
#     print(item.text)
#     print(item.answer)
#     print("")

# ------test section:------
# question_bank_test = []
# question_bank_test.append(Question("something", "True"))
# quiz_brain = QuizBrain(question_bank_test)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score {quiz.score}/{len(quiz.questions_list)}")