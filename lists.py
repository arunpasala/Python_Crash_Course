# list usually contains more than one element 
# its good idea to name elements in plural form.

bicyles= ['trek','cannondale','redline','specialized']
print(bicyles)

print(bicyles[0])
print(bicyles[0].upper())

print(bicyles[1])
print(bicyles[2])
print(bicyles[-1])
# -1 index is use full if do not know the last index of the list and like to print the last number.

message = f"my first cycle was a {bicyles[3].title()}"
print(message)

friends=['Arun','Jaya','Mani','Pavitra','Abhi']

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
# print(friends[5]) if we print the index without the value then it give indexError

message=f"Hello, I'm {friends[0].capitalize()}"
print(message)

message=f"Hello, I'm {friends[1].capitalize()}"
print(message)

message=f"Hello, I'm {friends[2].capitalize()}"
print(message)

message=f"Hello, I'm {friends[3].capitalize()}"
print(message)

message=f"Hello, I'm {friends[4].capitalize()}"
print(message)
# adding to index by number
friends[4]='vinay'

print(friends)

# appending

friends.append('raju')

print(friends[0].upper())

# Appending to empty list
motorcycles=[]

print(motorcycles)

motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
print(motorcycles[0].title())

# inserting elements into list
print(f"inserting an element into\n{motorcycles}")
motorcycles.insert(0,'yamaha')
motorcycles.insert(3,'vespa')
print(motorcycles)

# removing an element from list
print(f"removing an element from the list \n {motorcycles}"
      )
del motorcycles[3]
print(motorcycles)

# Removing and element using pop() Method

print(f"removing and element using the pop() Method from \n{motorcycles}")

popped_motorcycles = motorcycles.pop()
print(f"motorcycles: {motorcycles}")
print(f"popped_motorcycles: {popped_motorcycles}")


# popping items from any position in a list
print(f"popping an element from any positon {motorcycles}")
lastUsed=motorcycles.pop(1)
print(motorcycles)
print(f"my last used motorcycle was: {lastUsed.title()}")

# removing and element my value
print(motorcycles)
print(motorcycles.remove('suzuki'))
print(motorcycles)

# 3.4 try it your self
invite=[]
invite.append('Jaya')
invite.append('Mani')
invite.append('Pavi')
msg = "we are celebrating a dinner party please come "
print(invite)
# invitation for dinner
print(f"{msg} : {invite[0]}")
print(f"{msg} : {invite[1]}")
print(f"{msg} : {invite[2]}")

# 3.5 changing guest list
print(invite)
cant_make_it = invite.pop(1)
print(f"{cant_make_it} cannot make it")
print(invite)
invite.append('vinay')
print(invite)
print(f"{msg} : {invite[0]}")
print(f"{msg} : {invite[1]}")
print(f"{msg} : {invite[2]}")
# 3.6
# adding new guest

invite.insert(2,"raj")
print(invite)

invite.insert(1,'paul')
print(invite)

invite.append('pinky')
print(invite)
print(f"{msg} : {invite[0]}")
print(f"{msg} : {invite[1]}")
print(f"{msg} : {invite[2]}")
print(f"{msg} : {invite[3]}")
print(f"{msg} : {invite[4]}")
print(f"{msg} : {invite[5]}")

msg2 ="I can only invite two person as the table is not arried by the time."
print(msg2)

invite.pop()
print(invite)
invite.pop()
print(invite)
invite.pop()
print(invite)
invite.pop()
print(invite)

msg3= "You are still invited"

print(f"{msg3} : {invite[0]}, {invite[1]}")

del invite[0]
print(invite)

del invite[0]
print(invite)