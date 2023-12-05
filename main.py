from data import question_data
from quiz_brain import QuizBrain
from consquest import ConstQuest
import random
from data import question_data_2

# database 1
bank1 = ConstQuest(q_list=question_data, text="text", answer="answer")
bank1_to = bank1.question_convert()
# print(bank1_to)
# database 2
bank2 = ConstQuest(q_list=question_data_2, text="question", answer="correct_answer")
bank2_to = bank2.question_convert()
# print(bank2_to)

bank1_to_quiz = QuizBrain(bank1_to)
bank2_to_quiz = QuizBrain(bank2_to)
# bank1_to_quiz.next_question()
bank2_to_quiz.next_question()




