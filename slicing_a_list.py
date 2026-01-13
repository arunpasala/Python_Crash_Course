#slicing a list mean extracting a part of list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#slicing first three players    
print("Here are the first three players on my team:")
for player in players[:3]:  
    print(player.title())           
#slicing middle three players
print("Here are the middle three players on my team:")      
for player in players[1:4]:  
    print(player.title())
#slicing last three players
print("Here are the last three players on my team:")
for player in players[-3:]:  
    print(player.title())
    
#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#adding different food items to both lists
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
#The original list is not affected when we modify the copy of the list.