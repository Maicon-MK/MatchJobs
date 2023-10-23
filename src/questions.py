class Questions:
    def __init__(self):
        self.valid_options = ['A', 'B', 'C', 'D']
        self.intense_options = ['Nenhuma','Pouco','Bastante','Demais']

    def ask_question(self, question_text):
        answer = input(question_text).capitalize().strip()
        if answer not in self.valid_options:
            raise ValueError('Opção inválida!')
        else:
            return answer

    def question(self):
        for option in self.valid_options:
            for intense in self.intense_options:
                print (f'{option}. {intense}')

    def first_question(self):
        return self.ask_question('''Qual é o que?
    A. Blablabla
    B. Blablabla
    C. Claclacla
    D. Doideira\n''')

    def second_question(self):
        return self.ask_question('''Qual é o que?
    A. Blablabla
    B. Blablabla
    C. Claclacla
    D. Doideira\n''')

    def third_question(self):
        return self.ask_question('''Qual é o que?
    A. Blablabla
    B. Blablabla
    C. Claclacla
    D. Doideira\n''')

    def fourth_question(self):
        return self.ask_question('''Qual é o que?
    A. Blablabla
    B. Blablabla
    C. Claclacla
    D. Doideira\n''')

