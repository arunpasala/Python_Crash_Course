class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
         """simulate rolling over in response to a command"""
         print(f"{self.name} rolled over!")    
    
my_dog = Dog("robbin", 2)

print(my_dog.name)   # robbin
print(my_dog.age)    # 2

my_dog.sit()
my_dog.roll_over()