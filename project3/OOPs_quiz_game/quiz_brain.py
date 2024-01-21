class QuizBrain:
    def __init__(self,lst):
        self.question_number = 0
        self.question_list = lst
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_ans,current_question.answer)


    def still_has_questions(self):
        if self.question_number < len(self.question_list):       #return self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self,user_ans,correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.score +=1
            print("You got it right!")

        else:
            print("You got it wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"score: {self.score}/{self.question_number}")
        print("\n")

    def finale(self):
        print("You have completed the quiz!")
        print(f"Your final score is: {self.score}/{self.question_number}")




