class Restaurant:
    """ Creating a restaurant class """
    def __init__(self, restaurant_name, cuisine_type):
        """ Initializes restaurant name and cuisine type """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Prints out restaurant name and cuisine type """
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """ Prints out a message indicating the restaurant is open """
        print(f"{self.restaurant_name} is now open.")
    
restaurant = Restaurant("Pizza Palace", "Kenyan")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()