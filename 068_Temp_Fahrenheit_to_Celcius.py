fahrenheit = float(input("Temperature (F): "))

# Convert the temperature from fahrenheit to celsius using the formula:
# https://en.wikipedia.org/wiki/Celsius
celsius = (fahrenheit - 32) / 1.8

# Output the temperature in Celsius
print("Temperature (C):", celsius)

# Alternatively, we could use an f-string to output the temperature with 
# 2 decimal digits of precision.
print(f"Temperature (C): {celsius:.2f}")