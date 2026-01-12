# A list  comprehension is a way to create a new list based on an existing list in a single line of code.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
squares = [x**2 for x in range(10)]
print(squares)  
# This code creates a list of squares of numbers from 0 to 9 using list comprehension.  
# The expression x**2 is evaluated for each value of x in the range from 0 to 9, and the resulting values are collected into a new list called squares.

# You can also add conditions to filter the elements that are included in the new list.
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares) 
# This code creates a list of squares of even numbers from 0 to 9.
# The if clause filters the values of x to include only those that are even (i.e., x % 2 == 0).
# The resulting list even_squares contains the squares of 0, 2, 4, 6, and 8.
# List comprehensions can also be used with more complex expressions and multiple for clauses.
combinations = [(x, y) for x in range(3) for y in range(5)]
print(combinations)
# This code creates a list of all possible combinations of pairs (x, y) where x and y both range from 0 to 2.
# The resulting list combinations contains the pairs (0, 0), (0, 1