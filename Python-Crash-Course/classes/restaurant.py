class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

restaurant1 = Restaurant("\nMama Nilishe", "Kenyan")
restaurant2 = Restaurant("\nGood Sushi", "Japanese")
restaurant3 = Restaurant("\nBig Fish", "Kenyan")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()