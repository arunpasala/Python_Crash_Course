from pathlib import Path

path = Path("Files_And_Exceptions/pi_digits.txt")
contents = path.read_text()
print(contents)



#Accessing a File's Lines

lines= contents.splitlines()
#splitlines == method to turn a long string into a set of lines, and thn use a for loop to examine
#each lines from a file, one at a time.                    
for line in lines:
    print(line)
    
    
#since, we havent modified any of the lines, the output matches the original text file exactly.
