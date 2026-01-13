#an immutable list is called tuple
# A tuple is similar to a list, but unlike lists, tuples are immutable, meaning their elements cannot be changed after creation
#tuples are defined using parentheses () instead of square brackets []
# We can access elements in a tuple using indexing, just like we do with lists
# However, since tuples are immutable, we cannot modify, add, or remove elements from them
dimensions = (200, 50)
print(dimensions[0])    
print(dimensions[1])
dimensions[0]=250  # This will raise an error because tuples are immutable
# However, we can redefine the entire tuple if needed
dimensions = (250, 50)
print(dimensions[0])
print(dimensions[1])