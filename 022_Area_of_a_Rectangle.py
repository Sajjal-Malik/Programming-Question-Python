def area_of_rectangle(length, width):
    return round(length * width, 4)

length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = area_of_rectangle(length, width)

print("Area of Rectangle is: " + str(area))
