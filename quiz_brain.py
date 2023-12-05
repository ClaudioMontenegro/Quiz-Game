import random


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        random_list = list(range(0, len(self.questions_list)))
        random.shuffle(random_list)
        for rn in random_list:
            current_question = self.questions_list[random_list[rn]]
            self.question_number += 1
            answer = input(f"Q.{self.question_number}: "
                           f"{current_question.text}"
                           f"(True/False)?: ")
            if answer.lower() == current_question.answer.lower():
                self.score += 1
                print("You got it right!")
            else:
                print(f"That's wrong.")
            print(f"The correct answer was: {current_question.answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")

        print(f"You've completed the quiz\n"
              f"Your final score was: "
              f"{self.score}/{self.question_number}")
