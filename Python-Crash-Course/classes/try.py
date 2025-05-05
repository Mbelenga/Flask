class Instructor:
    def __init__(self, Instructor_name, address):
        self.name = Instructor_name
        self.address = address

    def display(self, subject_name):
        print(f"Hi, I am {self.name} am learning {subject_name}")

Instructor_1 = Instructor("Mathew","Nairobi")
print(Instructor_1.name)
Instructor_1.display("Python")