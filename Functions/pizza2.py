#mixing postional and arbitary arguuments:
#If you want to a function to accept several different kinds of arguments, 
#the parameter that accepts an arbitary number of arguments must be placed last in the function defination.
def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")   
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')