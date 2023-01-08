
class QuizBrain:
    # score = 0
    def __init__(self,question_list) :
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def next_question(self):
        
    # for i in self.question_list:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer=input(f'Q.{self.question_number}: {current_question.question}(True/False):').title()
        self.check_answer(answer,current_question.correct_answer)
        # if answer == current_question.answer:
            #     score += 1
            #     print(f'You got it right\nThe answer was {current_question.answer}\nYour score is {score} / {self.question_number}')
            # else:
            #     print(f'You got it wrong\nThe answer was {current_question.answer}\nYour score is {score} / {self.question_number}')
                    
        # print()
        # print(f'Your score is {score} / {self.question_number}') 

    def check_answer(self, answer, correct_answer):
        
        
        if answer == correct_answer:
            self.score += 1
            print(f'You got it right\nThe answer was {correct_answer}\nYour score is {self.score} / {self.question_number}')
        else:
            print(f'You got it wrong\nThe answer was {correct_answer}\nYour score is {self.score} / {self.question_number}')
        print()
       
            


    
