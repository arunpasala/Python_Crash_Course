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

#keyword arguments: when we use keyword arguments, the order of the arguments does not matter.
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')  #Correct usage of keyword arguments
#default values: we can provide default values for parameters in the function definition.
def describe_pet2(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
#Avoiding argument errors: when you start writing functions, you may run into several types of argument errors. Here are some tips to help you avoid these errors:
#1.Missing arguments: when you call a function, Python matches the positional and keyword arguments you provide to the parameters in the function definition. If Python can’t match the arguments you provide to the parameters in the function definition, it raises a TypeError exception.