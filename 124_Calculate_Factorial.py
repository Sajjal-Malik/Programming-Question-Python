import math

# Or we can create our own.  This function returns the factorial of n by 
# calculating the product of all integers between n and 1.  It uses a 
# loop and counter variable to go through all of these integers, building
# the product one multiplication at a time using 'product'.  Notably 
# the function will still work for 0! n=0 as product is set to 1 and the
# loop will not execute at all in this case so we simply return 1.
def factorial(n):
    product = 1 
    for i in range(1,n+1): 
        product *= i
    return product

# Prompt the user to enter n, convert the string into an int type value and 
# store it into n
n = int(input("Enter n: "))

# Output an error message if n is not a non-negative integer, otherwise we 
# call the factorial function to calculate the product and output the result
if n < 0:
    print("n must be a non-negative integer")
else:
    product = factorial(n)
    print(product)

# We could also use the math module's factorial function
print(math.factorial(5))