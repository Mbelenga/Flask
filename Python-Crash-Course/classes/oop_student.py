"""
🚗 Python OOP Practice Question:
Create a class called Student with the following:

Attributes: name, age, and grade

A method called display_info() that prints:

"<name> is <age> years old and scored grade <grade>."

Then:

Create an object of the Student class with your own details.

Call the display_info() method on that object.
"""
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f" {self.name} is {self.age} years old and score grade {self.grade}")

my_student = Student('Mali', '3', 'B')
my_student.display_info()