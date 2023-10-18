import areas

"""
instanciar objetos correspondentes as areas
coletar os \" pontos \" dessas areas e exportar para um csv junto do nome do usuario
com o csv podemos fazer os inserts de um modo simples no banco de dados
TALVEZ fosse interessante, dependendo da pontuação inicial de alguma(s) area(s) nas primeiras perguntas 
genericas criar metodos exclusivos com perguntas para cada area
"""

class Questions:

    def __init__(self):
        self.area1 = areas()
        self.area2 = areas()
        self.area3 = areas()
        self.area4 = areas()
        pass

    def genericas(self):
        pergunta_1 = input('A, B, C, D').capitalize().strip()
        if pergunta_1 == 'A':
            self.area1.recebe(1)
        elif pergunta_1 == 'B':
            self.area2.recebe(1)
        elif pergunta_1 == 'C':
            self.area3.recebe(1)
        elif pergunta_1 == 'D':
            self.area4.recebe(1)
        
    def exportar_resultados(self):
        # exportar para um csv
        ...