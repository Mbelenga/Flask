class Building
    def __init__(self, address):
        self.address = address
    
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

class Appartment(Building):
    def __init__(self, address, floor_number):
        super().__init__(address)
        self.floor_number = floor_number
    
    def describe(self):
        return f"This appartment is on floor {self.floor_number}"

buildings = [House('Syokimau', '182000'), Appartment('Elm street', 90)]
for building in buildings:
    print(building.describe())
