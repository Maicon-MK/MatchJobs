class Questions:
    def __init__(self):
        self.valid_options = ['A', 'B', 'C', 'D']
        self.intense_options = ['Demais','Sim','Um pouco','Não']
        self.questions = ['1. Você se considera uma pessoa preditiva?',
                          '2. Você se considera uma pessoa com alto pensamento critico?',
                          '3. Você se considera uma pessoa criativa?',
                          '4. Você se considera uma pessoa comunicativa?']

    def get_answer(self):
        answer = input().capitalize().strip()
        if answer not in self.valid_options:
            raise ValueError('Opção inválida!')
        else:
            return answer

    def question(self, question_index):
        print(self.questions[question_index])
        for option in self.valid_options:
            print (f'{option}. {self.intense_options[self.valid_options.index(option)]}')
        return self.get_answer()
