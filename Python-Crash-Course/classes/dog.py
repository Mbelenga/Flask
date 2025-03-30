"""
Write a Python class called Dog that:

Has an __init__ method to initialize two attributes: name and age.

Contains a method sit() that prints a message indicating the dog is sitting.

Contains another method roll_over() that prints a message indicating the dog is rolling over.

Create an instance of the Dog class with the name "Rio" and age 8.

Print the dog's name and age using formatted strings.
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog = Dog("Rio", 8)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()