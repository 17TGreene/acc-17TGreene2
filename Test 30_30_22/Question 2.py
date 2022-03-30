import math

myH = float(input("Enter the height of the cylinder."))
myR = float(input("Enter the radius of the cylinder."))

def Volume(h,r):
    vol = h*(r**2)*(math.pi)
    return vol



print(Volume(myH,myR))
    