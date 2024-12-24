def third_angle_of_triangle(angle1, angle2):
    if ((angle1 > 0 and angle1 < 180) and (angle2 > 0 and angle2 < 180) and ((angle1 + angle2) < 180)):
        angle3 = 180 - angle1 - angle2
        print("Angle 3 is: " + str(angle3))
    else:
        print("Angle 1 and/or Angle 2 is invalid!")

angle1 = float(input("Angle 1: "))
angle2 = float(input("Angle 2: "))

third_angle_of_triangle(angle1, angle2)