class Areas:
    def __init__(self,name):
        self.name = name
        self.area = {self.name:0}

    def quantity(self) -> str:
        return self.area[self.name]

    def receives(self, quantity):
        self.area[self.name] += quantity

