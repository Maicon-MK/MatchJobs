"""
menu com as perguntas e cada area irá receber um ponto dependendo da pergunta
"""


from src.interview import Interview

name = input('Qual é o seu nome? ').capitalize().strip()
Interview(name).interview()