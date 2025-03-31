class Car:
    """ A car class """
    
    def __init__(self, make, model, year):
        """Initializing attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """prints the odometer reading"""
        print(f"This car has {self.odometer_reading} miles on it")

my_new_car = Car('audi', 'a4', '2025')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()