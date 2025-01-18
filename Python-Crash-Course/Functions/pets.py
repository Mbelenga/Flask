# The function tells us what kind of animal each pet is and the name of the pet.
def describe_pet(animal_type, pet_name):
    """Displays information about the pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog', 'Rio')
describe_pet('dog', 'Oki')
describe_pet('dog', 'Snooby')
describe_pet('cat', 'Grey')