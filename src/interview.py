from src.areas import Areas
from src.questions import Questions
import pandas as pd

"""
instanciar objetos correspondentes as areas
coletar os \" pontos \" dessas areas e exportar para um csv junto do nome do usuario
com o csv podemos fazer os inserts de um modo simples no banco de dados
TALVEZ fosse interessante, dependendo da pontuação inicial de alguma(s) area(s) nas primeiras perguntas 
genericas criar metodos exclusivos com perguntas para cada area
seria interessante criar uma variavel que recebe o a alternativa escolhida, asssim definindo
qual seria a proxima pergunta com base na resposta da anterior
calculo de porcentagem feito durante esta classe ou depois analisando o conteudo do banco de dados?
"""

class Interview:
    def __init__(self, name):
        self.name = name
        self.questions = Questions()
        self.area1 = Areas('area1')
        self.area2 = Areas('area2')
        self.area3 = Areas('area3')
        self.area4 = Areas('area4')

    def interview(self):
        answer1 = self.questions.first_question()
        if answer1 == 'A':
            self.area1.receives(1)
        elif answer1 == 'B':
            self.area2.receives(1)
        elif answer1 == 'C':
            self.area3.receives(1)
        elif answer1 == 'D':
            self.area4.receives(1)

        answer2 = self.questions.second_question()
        if answer2 == 'A':
            self.area1.receives(1)
        elif answer2 == 'B':
            self.area2.receives(1)
        elif answer2 == 'C':
            self.area3.receives(1)
        elif answer2 == 'D':
            self.area4.receives(1)

        answer3 = self.questions.third_question()
        if answer3 == 'A':
            self.area1.receives(1)
        elif answer3 == 'B':
            self.area2.receives(1)
        elif answer3 == 'C':
            self.area3.receives(1)
        elif answer3 == 'D':
            self.area4.receives(1)

        answer4 = self.questions.fourth_question()
        if answer4 == 'A':
            self.area1.receives(1)
        elif answer4 == 'B':
            self.area2.receives(1)
        elif answer4 == 'C':
            self.area3.receives(1)
        elif answer4 == 'D':
            self.area4.receives(1)


    def exportar_resultados(self):
        resultados = {'nome':self.name, 
                      'area1':self.area1.quantity(), 
                      'area2':self.area2.quantity(),
                      'area3':self.area3.quantity(),
                      'area4':self.area4.quantity()}

        return pd.DataFrame(resultados).to_csv('data/dados.csv',index=False)

