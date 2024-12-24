def area_of_square(side):
    return round(side ** 2, 4)

side = float(input("Side Length: "))

area = area_of_square(side)

print("Area: " + str(area))