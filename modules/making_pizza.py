import pizza
print('\nimporing firectly from file')
pizza.make_pizza(16,'pepproni')
pizza.make_pizza(18,'onion','capsicum','pepproni')

#You can also import a specific function from a module. Here's the general syntax for this approach
#from module_name import function_name

#You can also import as many functions as you want from a module by separating each functions name with a comma
#from module_name import function_0, function_1, function_2

from pizza import make_pizza

print('\nImporting by name')
make_pizza(12, 'tomato','cheese')
make_pizza(8, 'garlic parmasan')

#above code are same but the import format is different, with this syntax we dont need to use the dot notation
#when you call a function. Because, we've explicitly imported the function make_pizza() in the import statement,
#we can call it by name when we use the function.


############################################
#Using as to give a function an alias
#IF the name of a function you're importing might conflict with an existing name in your program of if the function name is long,
#you can use a short, unique alias- an alternate name similar to a nickname when you import the function

from pizza import make_pizza as mp

print("\nUsing alias as mp"
)
mp(16, 'cheese')
mp(18, "pepproni")


#We also use alias to a module
import pizza as p
p.make_pizza(16,"topping")

#importing all functions in a module
# we use (*) to import every function in the module
from pizza import *
make_pizza(8,"olives")
