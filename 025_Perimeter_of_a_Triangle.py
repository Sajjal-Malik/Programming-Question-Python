def perimater_of_triangle(side_A, side_B, side_C):
    return round(side_A + side_B + side_C, 2)

side_A = float(input("Side A: "))
side_B = float(input("Side B: "))
side_C = float(input("Side C: "))

perimeter = perimater_of_triangle(side_A, side_B, side_C)

print("Perimeter: " + str(perimeter))