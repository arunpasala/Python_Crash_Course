from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give first name: ")
    if first == 'q':
        break
    last = input("\nPlease give last name: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first,last)
    print(f"\t neatly formatted name: {formatted_name}")