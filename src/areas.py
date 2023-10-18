class Areas:
    def __init__(self,name):
        self.name = name
        self.area = {self.name:0}

    def recebe(self, quantidade):
        self.area[self.name] += quantidade

