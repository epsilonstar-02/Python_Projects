class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        ques = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number +1}: {ques.question}")
        self.question_number += 1
        self.check_answer(ques,ans)
        return ans

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,ques, ans):
        if ans == ques.answer:
            print(f"Right answer!!!")
            self.score += 1
            print(f"Score: {self.score}/{self.question_number}")
        else:
            print(f"Wrong Answer!!!")
            print(f"Correct Answer is: {ques.answer}")
            print(f"Score: {self.score}/{self.question_number}")
        print("\n")