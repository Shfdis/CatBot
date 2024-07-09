from QuizInterface import *
from Question import *
from Cat import *
class Test(Test_I):
    def input_stats(self,f) -> dict:
        m = int(f.readline())
        stats = {}
        for i in range(m):
            stat, points = map(str,f.readline().strip('\n').split())
            points = int(points)
            stats.update({stat:points})
        return stats
    
    def input_answers(self,f) -> list:
        n = int(f.readline())
        answers = []
        for i in range(n):
            anstext = f.readline().strip('\n')
            answers.append(Answer(anstext,self.input_stats(f)))
        return answers
    
    def input_questions(self,f) -> list:
        amount = int(f.readline())
        questions = []
        for i in range(amount):
            questext = f.readline().strip('\n')
            questions.append(Question(questext,self.input_answers(f)))
        return questions
    
    def input_cats(self,f) -> list:
        k = int(f.readline())
        cats = []
        for i in range(k):
            name = f.readline().strip('\n')
            description = f.readline().strip('\n')
            photo = f.readline().strip('\n')
            cats.append(Cat(name, description, photo, self.input_stats(f)))
        return cats

    def __init__(self):
        f = open(r'Catques.txt')
        self.disclaimer = f.readline().strip('\n')
        self.questions = self.input_questions(f)
        self.cats = self.input_cats(f)

    def start(self):
        self.numberques = 0
        self.user_answers = []
        return self.disclaimer
    
    def ask_question(self):
        return self.questions[self.numberques]
    
    def get_answer(self, answer: str):
        for i in self.questions[self.numberques].answers:
            if i.ans == answer:
                self.user_answers.append(i)
                return True
        return False
    