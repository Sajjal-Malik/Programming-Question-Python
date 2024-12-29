while True:

    # Prompts the user to enter the integer, converts the text entered by the 
    # user and returned by input() from a string to an int value and stores 
    # it into decimal
    decimal = int(input("Enter A Non-Negative Integer: "))

    # If decimal is a negative integer reminder the user the integer must 
    # be non-negative
    if decimal < 0:
        print("Integer Must Be A Non-Negative Integer")
    else:
        # Stops the loop once decimal is a non-negative integer
        break 

# Stores the binary number, represented as a string of 1s and 0s
binary = ""

# Implements the algorithm described above, repeatedly dividing the number by 2
while True:

    # divmod() will return both the quotient and remainder of decimal / 2, we 
    # notably store the quotient back into decimal as we want the quotient of 
    # the previous division operation to become the new decimal number in the 
    # next division operation
    decimal, remainder = divmod(decimal, 2)

    # We essentially "prepend" the next binary number digit onto the front of 
    # the binary number (represented as a string) using the string concatenation
    # operation '+'.  This will build the binary number in the correct order, as
    # noted above the leading digit of the binary number will be the remainder 
    # of the last division operation.
    binary = str(remainder) + binary 

    # Stops the loop/algorithm when the quotient reaches 0
    if decimal == 0:
        break 

# Output the resulting binary number
print(binary)