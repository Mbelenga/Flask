class Car:
    """ A car class """
    
    def __init__(self, make, model, year):
        """Initializing attributes"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

my_new_car = Car('audi', 'a4', '2025')
print(my_new_car.get_descriptive_name())
