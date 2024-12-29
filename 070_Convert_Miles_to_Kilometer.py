miles = float(input("Miles: "))

# Convert the distance to kilometers and store it into the variable miles using
# the formula: https://en.wikipedia.org/wiki/Kilometre
kilometers = miles / 0.621371

# Output the text "Kilometers:" followed by the value in the variable kilometers
print("Kilometers:", kilometers)
 
# Alternatively, we could use an f-string to output the kilometers with 
# 2 decimal digits of precision with .2 and in fixed-point notation with .2f
print(f"Kilometers: {kilometers:.2f}")