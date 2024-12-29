# Prompt user for filename, text to find, and replacement text
filename = input("Filename: ")
find = input("Find Text: ")
replace = input("New Text: ")

# Open the file for reading, read all file text and store into the variable 
# contents, and then create new contents string by replacing all text to find
# with the replacement text
with open(filename) as file:
  contents = file.read()
  contents = contents.replace(find,replace)

# Open the file for writing and write the new contents string to the file as the
# file contents
with open(filename, "w") as file:
  file.write(contents)