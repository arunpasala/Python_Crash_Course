# Organizing a list
# sorting a list permanently with the sort() method

cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.sort()
print(f"sorted: {cars}")

cars.sort(reverse=True)
print(f"reverse sorted: {cars}")

# sorting a list temporarily with the sorted() function

cars = ['bmw','audi','toyota','subaru']
print(cars)
print(f"Here is the original list \n {cars}")
print(f"Here is the sorted list \n {sorted(cars)}")
print(f"Here is the Original list again \n {(cars)}")

len(cars)