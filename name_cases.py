
# 2.3 printing name with the message using f-string
name= "raj"
print(f"Hello, {name} would you like to learn some python? ")
# 2.4 Cases(lower, upper, title)
print(name.upper())  
print(name.title())
print(name.lower())

# 2.5 & 2.6 printing quote with a person name
person_name = "Arun Pasala"
quote ="Live and let live"

print(f' {person_name} once said, {quote}. ')

#2.7 stripping Names

person_name = " Arun "
print(f"next line: \n{person_name}")
print(f" tab: \t{person_name}")
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())


# File extensions remove prefix and suffix

filename = "python_notes.txt"
print(filename)
print(filename.removesuffix(".txt"))
print(filename.removeprefix("python_notes"))

