from os import system
from src.utils_interview import Utils
from src.questions import Questions

class Interview:
    def __init__(self,name):
        self.name = name
        self.utils = Utils(self.name)
        self.questions = Questions()

    def get_results(self):
        return self.utils.results()

    def interview(self):
        system('cls')
        answer1 = self.questions.question(0)
        self.utils.verification(answer1)
        system('cls')
        answer2 = self.questions.question(1)
        self.utils.verification(answer2)
        system('cls')
        answer3 = self.questions.question(2)
        self.utils.verification(answer3)
        system('cls')
        answer4 = self.questions.question(3)
        self.utils.verification(answer4)
        system('cls')
