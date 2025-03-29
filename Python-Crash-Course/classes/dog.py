class Dog:
    """A simple attempt to model a dog"""

def __init__(self, name, age):
    """Initializes name and age attributes"""
    self.name = name
    self.age = age

def sit(self):
    print(f"{self.name} is now sitting")

def roll_over(self):
    print(f"{self.name} is now rolling over")

my_dog = Dog('Rio', 7)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")