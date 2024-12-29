import math

# Returns the volume of a sphere with radius r.  Note that r ** 3 will give us 
# the radius r to the power of 3.
def sphere_volume(r):
  return (4/3) * math.pi * (r ** 3)

# Prompt the user to enter in the radius using input(), the input() function 
# returns the string the user enters, which we convert to a float value with 
# float() before assigning the value to radius.
radius = float(input("Radius: "))

# Calculate the volume of the sphere using our function, passing the radius the
# user entered as an argument
volume = sphere_volume(radius)

# Output the calculated sphere volume
print("Sphere Volume: ")
print(volume)