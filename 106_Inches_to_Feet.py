total_inches = int(input("Inches: "))

# The built-in divmod() function will return the quotient and remainder of 
# dividing total_inches by 12.  The quotient will be the number of feet (as 
# there are 12 inches in a foot) and the remainder will be any inches left 
# over after accounting for the number of feet.  The divmod() function returns 
# a tuple, and we store each of the two values into the tuple into the 
# variables feet (quotient) and inches (remainder).
feet, inches = divmod(total_inches, 12)

# Output the total number of feet and inches (note that by default print() 
# will separate the values it outputs by once space).
print(feet, "feet", inches, "inches")