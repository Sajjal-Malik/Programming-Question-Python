def area_of_triangle(base, height):
    return round(0.5 * base * height, 4)

base = float(input("Enter Base: "))
height = float(input("Enter Width: "))

area = area_of_triangle(base, height)

print("Area of Triangle is: " + str(area))
