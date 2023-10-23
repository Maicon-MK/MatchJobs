from src.areas import Areas
from src.questions import Questions
import pandas as pd
from os import system, path
from time import sleep

class Interview:
    def __init__(self, name):
        self.name = name
        self.questions = Questions()
        self.area1 = Areas('Análise de Dados')
        self.area2 = Areas('Backend')
        self.area3 = Areas('Frontend')
        self.area4 = Areas('Produto')

    def interview(self):
        system('cls')
        answer1 = self.questions.question(0)
        if answer1 == 'A':
            self.area1.receives(1)
        elif answer1 == 'B':
            self.area2.receives(1)
        elif answer1 == 'C':
            self.area3.receives(1)
        elif answer1 == 'D':
            self.area4.receives(1)

        system('cls')
        answer2 = self.questions.question(1)
        if answer2 == 'A':
            self.area1.receives(1)
        elif answer2 == 'B':
            self.area2.receives(1)
        elif answer2 == 'C':
            self.area3.receives(1)
        elif answer2 == 'D':
            self.area4.receives(1)

        system('cls')
        answer3 = self.questions.question(2)
        if answer3 == 'A':
            self.area1.receives(1)
        elif answer3 == 'B':
            self.area2.receives(1)
        elif answer3 == 'C':
            self.area3.receives(1)
        elif answer3 == 'D':
            self.area4.receives(1)

        system('cls')
        answer4 = self.questions.question(3)
        if answer4 == 'A':
            self.area1.receives(1)
        elif answer4 == 'B':
            self.area2.receives(1)
        elif answer4 == 'C':
            self.area3.receives(1)
        elif answer4 == 'D':
            self.area4.receives(1)
        system('cls')

        results = {'Nome': [self.name], 
                    'Análise de Dados': [self.area1.quantity()], 
                    'Frontend': [self.area2.quantity()],
                    'Backend': [self.area3.quantity()],
                    'Produto': [self.area4.quantity()]}
        
        return results




