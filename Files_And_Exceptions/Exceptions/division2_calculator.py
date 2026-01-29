print("Give me two number and i will divide them")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First number")
    if first_number == 'q':
        break
    second_number = input("\n Second number")
    if second_number == 'q':
        break
    try:
       answer = int(first_number)/int(second_number)
       print(answer)
    except ZeroDivisionError:
        print("Not divisible by 0")
    else:
        print(answer)