class Questions:
    def __init__(self):
        self.valid_options = ['A', 'B', 'C', 'D']

    def ask_question(self, question_text):
        answer = input(question_text).capitalize().strip()
        if answer not in self.valid_options:
            raise ValueError('Opção inválida!')
        else:
            return answer

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

