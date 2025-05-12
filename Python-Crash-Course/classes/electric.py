class ElectricCar(Car):
    """ Aspect of a car specific to electric vehicles """
    def __init__(self, make, model, year):
        """ It Initializes attributes """
        super().__init__(make, model, year)
my_leaf = ElectricCar("Nissan", "Leaf", "2024")
print(my_leaf.get_descriptive_name())