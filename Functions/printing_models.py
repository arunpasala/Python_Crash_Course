#modifying a list in a function
#Any changes made to a list inside a function's body are permanent, because lists are mutable objects.
#MUTABLE OBJECTS: Lists, dictionaries, sets, and most user-defined classes are mutable objects. 
# This means that their contents can be changed after they are created.

#Design that need to be printed

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #simulate printing each design, until none are left.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
    
#     #simulate creating a 3D print from the design.
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
# #Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
    
# --- IGNORE ---
#Note: If you pass a copy of a list to a function, the original list will remain unchanged.
#To send a copy of a list to a function, you can slice off all the items in the list by
#including a colon in the brackets.
#for example: function_name(list_name[:])
#Here is an example:
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        #simulate creating a 3D print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)



