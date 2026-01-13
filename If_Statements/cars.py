# 4.6` if statements: cars`
# Using if-else statement to print car names in different formats
# 'bmw' is printed in uppercase, others in title case
# List of car brands
# Define a list of car brands

cars = ["audi", "bmw", "subaru", "toyota"]
# Iterate through the list and apply conditional formatting
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
        
# The code checks if the car brand is 'bmw' and prints it in uppercase.
# For all other car brands, it prints the name in title case.   
# This demonstrates the use of if-else statements to apply different formatting based on conditions.