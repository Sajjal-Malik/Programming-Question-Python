def file_average(filename):
  
  # opens the file for reading, file will be a reference to the file object
  file = open(filename)
  
  # readlines() will read each line from the file and store it as a string in 
  # a list 
  number_list = file.readlines()
  
  # We'll need to total the numbers in the file, so create a variable total and 
  # initialize it to 0
  total = 0
  
  # Loop through each number in number_list and add it to the total, note that 
  # because each line of the file (i.e. each number) is stored as a string we
  # conver it to a floating-point number with float() before adding it to the 
  # total.
  for number in number_list:
    total = total + float(number)
  
  # Close our access to the file since we are done working with
  file.close()
  
  # len() will return the number of elements in the list (i.e. the total amount 
  # of numbers), we divide the total of the numbers by the total amount of 
  # numbers to compute and return the average.
  return total / len(number_list)

# Prompt the user to enter the filename, store it into input_filename
input_filename = input("File: ")

# Use the function with the supplied filename to compute the average
average = file_average(input_filename)

# Output the average
print("Average:", average)