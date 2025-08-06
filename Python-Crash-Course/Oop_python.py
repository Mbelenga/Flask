class Building:
    def __init__(self, address):
        self.address = adress
    
    def describe(self):
        return f"This building is at {self.address}"

class House(Building):
    def __init__(self, address, garden_size):
        super().__init__(address)
        self.garden_size = garden_size