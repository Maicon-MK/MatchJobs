from src.areas import Areas
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

class Questions:

    def __init__(self,name):
        self.name = name
        self.area1 = Areas('area1')
        self.area2 = Areas('area2')
        self.area3 = Areas('area3')
        self.area4 = Areas('area4')

    def genericas(self):
        pergunta_1 = input('A, B, C, D\n').capitalize().strip()
        if pergunta_1 == 'A':
            self.area1.recebe(1)
        elif pergunta_1 == 'B':
            self.area2.recebe(1)
        elif pergunta_1 == 'C':
            self.area3.recebe(1)
        elif pergunta_1 == 'D':
            self.area4.recebe(1)
        else:
            return 'Opção inválida'

    def exportar_resultados(self):
        resultados = {'nome':self.name, 
                      'area1':self.area1.quantidade(), 
                      'area2':self.area2.quantidade(),
                      'area3':self.area3.quantidade(),
                      'area4':self.area4.quantidade()}

        return pd.DataFrame(resultados).to_csv('data/dados.csv',index=False)
