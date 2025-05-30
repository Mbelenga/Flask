class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"Am driving an {self.model} {self.brand} {self.year} car")
    
my_car = Car('Mercedes', 'E200', 2007)
my_car.drive()