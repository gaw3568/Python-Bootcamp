class QuizBrain:
    
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    
    def next_question(self):
        # 현재 질문 번호의 항목 가져오기
        # question_list의 n번째 객체 가져오기
        recent_question = self.question_list[self.question_number]
        self.question_number += 1
        # input() 함수를 이용해 사용자에게 질문 text를 보여주고 사용자에게 답을 요청
        user_answer = input(f"Q.{self.question_number} : {recent_question.text} (True / False) : ")
        self.check_answer(user_answer, recent_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("정답")
            self.score += 1
        else:
            print(f"틀렸음. 정답은 {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")