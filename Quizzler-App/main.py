from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

# API에서 불러온 json파일에서 원하는 부분을 추출하여 
# question_bank 리스트에 저장
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

# 새로운 quiz_ui 객체를 생성하면서 생성자 메서드를 통해
# 자동으로 tkinter 실행
quiz_ui = QuizInterface(quiz)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
