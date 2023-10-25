class Areas:
    def __init__(self,name):
        self.name = name
        self.area = {self.name:0}

    def quantity(self) -> int:
        return self.area[self.name]

    def receives(self, quantity) -> int:
        self.area[self.name] += quantity
        return self.area[self.name]
