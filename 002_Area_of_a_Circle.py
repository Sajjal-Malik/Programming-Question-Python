from math import pi

def calculateArea(radius):
    area = pi * radius ** 2
    return round(area, 5)


radius = float(input("Radius: "))
area = calculateArea(radius)
print("Area of Circle -> ", area)