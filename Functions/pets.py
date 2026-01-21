#positional arguments: Python must match the order of the parameters in the function definition.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#values matched this way are called positional arguments because their position matters.
#order matter in positional arguments. If we swap the order of the arguments in the fuction call, we will get incorrect results.
describe_pet('willie', 'dog')  #Incorrect usage of positional arguments