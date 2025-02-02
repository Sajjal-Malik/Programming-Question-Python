# Returns the number of digits in the number
def count_digits(number):

  # Stores running count of digits in the number
  digits = 0
  
  # So long as the number has not yet reached 0, take the number and divide it
  # by 10 and store the resulting quotient back into the number.  Increment 
  # digits each time by 1 to acknowledge there is another digit in the number.
  while number != 0:
    number = number // 10 
    digits += 1
  
  # Return the number of digits in the number
  return digits 


# Returns true if the number n is an Armstrong number and false otherwise
def is_armstrong(n):
  
  # Find the number of digits in the number using the above function and store
  # the resulting return value into the variable number_of_digits
  number_of_digits = count_digits(n)
  
  # Following the same process as in count_digits, we'll go through each digit
  # in the number n.  This will involve modifying the number.  We still need 
  # a copy of the 'original number' because we'll be comparing the original 
  # number to the sum of each digit of the number raised to the power of the 
  # number of digits in the number to determine if the number is an Armstrong
  # number or  not.  So we make a copy of the number n, called temp.
  temp = n 

  # Will store the running sum of each digit in the number raised to the power
  # of the number of digits in the number
  sum = 0
  
  # Extracts each digit in the number, raises it to the power of the number of 
  # digits in the number, and adds the resulting number to sum.  The number 
  # is continually divided by 10 until it is equal to 0 (at which point the 
  # loop stops) in order to go through each digit in the number
  while temp != 0:

    # Extract the digit using modulus which returns the remainder of dividing
    # the number by 10
    digit = temp % 10

    # Take the number and divide it by 10, so we can keep going through the 
    # number one digit at a time
    temp = temp // 10

    # Take the digit, raise it to the power of number of digits using the power
    # operator **, and add the result to sum
    sum += digit ** number_of_digits

  # Check if the resulting sum is equal to n, if it is, the number is an 
  # Armstrong number and the function returns true, otherwise it is not an 
  # Armstrong number and the function returns false
  return sum == n

# Check if the number 153 is an Armstrong number (it is!)
print(is_armstrong(153))