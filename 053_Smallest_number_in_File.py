# Prompt the user to enter the name of the file to open, store it into filename
filename = input("Filename: ")

# Open the file with the provided filename for reading, use the readline() 
# method of the file object to get a list of strings of all lines in the file.
with open(filename) as file:
  lines_list = file.readlines()

# Use list comprehension to convert all strings in the file to float values
float_list = [float(n) for n in lines_list]

# min() will return the smallest float value in the list
smallest = min(float_list)

# Output the smallest value
print("Min:", smallest)