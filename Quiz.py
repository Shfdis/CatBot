from QuizInterface import *
from Question import *
from Cat import *
from input import *
class Test(Test_I):
    def results(self, cat):
        dist = 0
        user_stats = {}
        for i in self.user_answers:
            for j in i.stats:
                user_stats.update({j: 0})
        for i in self.user_answers:
            for j in i.stats:
                if j in self.stat:
                    user_stats[self.stat[j]] -= i.stats[j]
                else:
                    user_stats[j] += i.stats[j]
        for i in cat.stats:
            if i in self.stat:
                sum = (user_stats[self.stat[i]] + cat.stats[i]) ** 2
            else:
                sum = (user_stats[i]- cat.stats[i])**2
            dist += sum
        return dist

    def __init__(self):
        f = open(r'Catques.txt',encoding='utf-8')
        self.disclaimer = f.readline().strip('\n')
        inp = Input()
        self.stat = inp.input_antonims(f)
        self.questions = inp.input_questions(f)
        self.cats = inp.input_cats(f)

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
                self.numberques += 1
                return True
        return False
    
    def end(self) -> Cat:
        comp = 10**100
        for i in self.cats:
            if comp > self.results(i):
                comp = self.results(i)
                name_cat = i
        return name_cat
    