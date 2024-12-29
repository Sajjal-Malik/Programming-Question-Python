kilometers = float(input("Kilometers: "))

# Convert the distance to miles and store it into the variable miles using the 
# formula: https://en.wikipedia.org/wiki/Kilometre
miles = 0.621371 * kilometers

# Output the text "Miles:" followed by the value in the variable miles
print("Miles:", miles)
 
# Alternatively, we could use an f-string to output the miles with 
# 2 decimal digits of precision with .2 and in fixed-point notation with .2f
print(f"Miles: {miles:.2f}")