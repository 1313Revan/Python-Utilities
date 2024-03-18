class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def more_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, u_answer, q_answer):
        if u_answer.lower() == q_answer.lower():
            self.score += 1
            print("\nThat's correct!")
        else:
            print("\nThat's incorrect.")
        print(f"The answer was '{q_answer}'")
        print(f"\nYour score is: {self.score}/{self.question_number}\n")
