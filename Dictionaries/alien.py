alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

#A dictionary is a collection of key value pairs
#You can add new key value pairs to a dictionary

#Accessing valuse in a dictionary

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

#Adding a new key value pair to a dictionary

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['name']='arun'

print(alien_0)

print("all the key values pairs are removed now but only age is added: ")
alien_0 ={'age':25}
print(alien_0)


#modifying values in a dictionary
print("The alien is green, nnow the age is replaced with color")
alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

print(alien_0)

