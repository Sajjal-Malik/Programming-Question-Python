def perimater_of_square(side_length):
    return round(side_length * 4, 2)

side_length = float(input("Side length: "))

perimeter = perimater_of_square(side_length)

print("Perimeter: " + str(perimeter))