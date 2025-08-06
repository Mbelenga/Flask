class Building:
    def __init__(self, address):
        self.address = adress
    
    def describe(self):
        return f"This building is at {self.address}"

class House(Building):
    def __init__(self, address, garden_size):
        super().__init__(address)
        self.garden_size = garden_size
    
    def describe(self):
        return f"This house is at {self.address} and is also a building"
    
    def describe_print(self):
        print(f"This house is blue and the garden is {self.garden_size} big")