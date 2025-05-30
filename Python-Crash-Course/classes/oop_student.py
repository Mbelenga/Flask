class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f" {self.name} is {self.age} years old and score grade {self.grade}")

my_student = Student('Mali', '3', 'B')
my_student.display_info()