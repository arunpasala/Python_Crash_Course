current_user = ['admin', 'john', 'sarah', 'mike', 'linda']
new_users = ['sarah', 'mike', 'kevin', 'anna', 'admin']
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_user]:
        print(f"Sorry {new_user}, that username is already taken. Please enter a new username.")
    else:
        print(f"Welcome {new_user}, your username is available.")