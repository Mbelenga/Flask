class Circle:
    pi = 3.14
    def __init__(self, radius=6):
        self.radius = radius
    
    def get_circumference(self):
        return 2 * self.pi * self.radius

Circle_1 = Circle(4)
print(Circle_1.get_circumference())

# Next task find the area of a rectangle