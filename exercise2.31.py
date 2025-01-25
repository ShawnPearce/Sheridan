import math
def calculation(radius):
    calc= (4/3)*math.pi*radius**3
    return calc
radius = 5

volume = calculation(radius)
print("The volume of a sphere with a radius " +str(radius) +" is " +str(volume))
