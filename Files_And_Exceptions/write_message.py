from pathlib import Path

path = Path('Files_And_Exceptions/programming.txt')
path.write_text("I love programming.\n")
print("Text one written.")
contents = "I love creating new games\n"
contents += "I also working with data."

with path.open("a") as file:
    file.write(contents)
