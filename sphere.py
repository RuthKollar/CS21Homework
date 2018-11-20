#Ruth Kollar
#CS21C Assignment 2
#Sphere.py
#Takes input of radius of a sphere
#Then calculates diameter, circumference, surface area, and volume of the sphere and prints it
#Diameter = 2*radius
#Circumference = 2*Pi*radius
#Surface Area = 4*Pi*radius**2
#Volume = (4//3)*Pi*radius**3


#Sets the value of Pi as 3.14
PI=3.14


#Takes user input for the value of the radius
#Stores radius value in variable R as a floating point number
radius = float(input('Enter the radius: '))

#Calculates diameter and stores in variable D
diameter = format(2*radius, '.1f')

#Calculates circumference and stores in variable C
circumference = format(2*PI*radius, '.1f')

#Calculates surface area and stores in variable SA
surface_area = format(4*PI*radius**2, '.1f')

#Calculates volume and stores in variable V
volume= format((4/3)*PI*radius**3, '.1f')

#Prints diameter, circumference, surface area, and volume on different lines
print("Diameter:",diameter, "\nCircumference:",circumference, "\nSurface Area:",surface_area, "\nVolume:",volume)


