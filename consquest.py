from question_model import Question


class ConstQuest:
    def __init__(self, q_list, text, answer):
        self.text = text
        self.answer = answer
        self.question_data = q_list

    def question_convert(self):
        question_bank = []
        n = 0
        for i in self.question_data:
            new_question = Question(self.question_data[n][self.text], self.question_data[n][self.answer])
            question_bank.append(new_question)
            # print(question_data[n][question], question_data[n][answer])
            n += 1
        return question_bank
