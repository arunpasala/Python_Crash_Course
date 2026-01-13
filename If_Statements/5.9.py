users = []

#if the list is empty we need to print a message saying we need to find some users
#remove all users from the list and run the program again to see the correct message
if users:
    for user in users:
        if user == "admin":
            print("Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
            
else:
    print("We need to find some users!")