# The function tells us what kind of animal each pet is and the name of the pet.
def describe_pet(animal_type, pet_name):
    """Displays the name of the pet"""
    print(f"\nThis is my {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog', 'willie')