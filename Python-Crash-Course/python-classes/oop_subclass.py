class SchoolMember:
    """ Represents any School Member """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized School Member: {}).format(self.name)")
    
    def tell(self):
        """ Tell my details """
        print('(Name: "{}" Age: "{}")'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    """ Represents a Teacher """
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("(Initialized Teacher: {}).format(self.name)")
    
    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{:d}"'.format(self.salary))

