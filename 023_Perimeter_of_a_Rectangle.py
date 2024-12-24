def perimater_of_rectangle(length, width):
    return round(2 * (length + width), 4)

length = float(input("Length: "))
width = float(input("Width: "))

perimeter = perimater_of_rectangle(length,  width)

print("Perimeter of Rectange: " + str(perimeter))