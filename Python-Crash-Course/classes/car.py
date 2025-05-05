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
    
    def update_odometer(self, mileage):
        """
        sets the odometer reding to the given value
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Adds the given amount to the odometer reading"""
        self.odometer_reading += miles

class Electricar(Car):
    """Car specific to electric vehicles"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_new_car = Electricar('Nissan', 'leaf', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25)
my_new_car.read_odometer()