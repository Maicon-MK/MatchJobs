"""
menu com as perguntas e cada area irá receber um ponto dependendo da pergunta

"""


from src.questions import Questions

name = input('Qual é o seu nome? ').capitalize().strip()
print(Questions(name).genericas())