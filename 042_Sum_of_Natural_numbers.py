n = int(input("Enter n: "))

# We can only sum the first natural numbers if n is greater than or equal to 1,
# we can't sum "the first -1 natural numbers".  So check to make sure that n
# is a valid value before attempting to find the sum of the first n natural
# numbers, and output an error message using the else case if it is not.
if (n >= 1):

  # Start the sum off at zero.
  sum = 0

  # Use number to keep track of the current natural number
  number = 1

  # Use a loop to go through the natural numbers from 1 up to n by 1, by
  # incrementing number by 1 with each loop iteration, and stopping the loop
  # when number exceeds n.  With each loop iteration we add the 'current natural
  # number' as given by number to the sum, in order to sum the natural numbers.
  while (number <= n):
    sum = sum + number
    number = number + 1

  # Output the resulting sum of the first n natural numbers
  print("Sum:", sum)

# Output an error message in the case that n is not greater than or equal to 1
# informing the user that n must be >= 1
else:
  print("n must be >= 1")