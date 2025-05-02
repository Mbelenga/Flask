class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        
    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"location: {self.location}")
    
    def greet_user(self):
        print(f"\nHello, {self.first_name}! Welcome Back")

user1 = User("Wakesho", "Mrashui", "24", "mrashuisophie@gmail.com", "Taita Hills")
user2 = User("Trivah", "Njoki", "26", "trivah101@gmail.com", "Machakos")
user3 = User("Tracy", "Maina", "21", "mainatracy@gmail.com", "Nairobi")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()