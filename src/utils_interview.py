from src.areas import Areas

class Utils:
    def __init__(self, name):
        self.name = name
        self.area1 = Areas('Produto')
        self.area2 = Areas('Backend')
        self.area3 = Areas('Frontend')

    def verification(self, answer):
        if answer == 'A':
            self.area1.receives(1)
        elif answer == 'B':
            self.area2.receives(1)
        elif answer == 'C':
            self.area3.receives(1)
        elif answer == 'D':
            self.area3.receives(1)

    def results(self):
        results = {'Nome': [self.name], 
                    'Produto': [self.area1.quantity()], 
                    'Frontend': [self.area2.quantity()],
                    'Backend': [self.area3.quantity()]}
        return results
