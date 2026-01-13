players=['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:  
    print(player.title())
print("Here are the middle three players on my team:")      
for player in players[1:4]:  
    print(player.title())
    
print("Here are the last three players on my team:")
for player in players[-3:]:
    print(player.title())
    
#copying a list
my_players = players[:]     
print("My players are:")
for player in my_players:
    print(player.title())

print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:  
    print(player.title())