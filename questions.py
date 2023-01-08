from data import question_data
from quiz_brain import QuizBrain

class Question:
    def __init__(self,question,correct_answer):
        self.question = question
        self.correct_answer = correct_answer


    
question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    qtn = Question(question_text,question_answer)
    question_bank .append(qtn)


quiz = QuizBrain(question_bank)
for i in question_bank:
    quiz.next_question()
    # new_qtn.check_answer()

print(f'You have completed the Quiz.\nYour final score is {quiz.score} / {quiz.question_number} ')


    # print(qtn.text,qtn.answer)
# q_1 = Question(question_data[1]['text'],question_data[1]['answer'])
# print(q_1.text)
# print(q_1.answer)

# for question in question_data:
#     print(question['text'])
#     print(question['answer'])
