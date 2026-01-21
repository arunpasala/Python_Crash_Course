#A function doesn't always have to display its output directly.
#Instead, it can process some data and then return a value of set of values.
# The value the function returns is called a return value.
def formatted_name(first_name , last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = formatted_name('jimi', 'hendrix')
print(musician)

#You can make an argument optional by giving it a default value.
def get_formatted_name(first_name , middle_name , last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'arun' , 'hendrix')
print(musician)

def get_formatted_name2(first_name , last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name2('jimi', 'hendrix')
print(musician)
musician = get_formatted_name2('jimi', 'hendrix', 'arun')
print(musician)