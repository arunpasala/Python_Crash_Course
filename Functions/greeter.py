def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello!, {username.title()}. ")
name=input("Enter your name: ")
greet_user(name)