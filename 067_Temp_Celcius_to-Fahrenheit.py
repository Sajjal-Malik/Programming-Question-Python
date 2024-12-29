celsius = float(input("Temperature (C): "))

# Convert the temperature from celsius to fahrenheit using the formula:
# https://en.wikipedia.org/wiki/Fahrenheit
fahrenheit = celsius * 1.8 + 32

# Output the temperature in Fahrenheit
print("Temperature (F):", fahrenheit)

# Alternatively, we could use an f-string to output the temperature with 
# 2 decimal digits of precision.
print(f"Temperature (F): {fahrenheit:.2f}")