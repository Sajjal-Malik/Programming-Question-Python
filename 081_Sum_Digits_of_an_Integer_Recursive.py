# Returns the sum of the digits in the integer value number
def sum_digits(number):
    remainder = number % 10
    if number // 10 == 0:
        return remainder 
    return remainder + sum_digits(number // 10)
     
# Test the function
print(sum_digits(472))