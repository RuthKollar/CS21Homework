#Ruth Kollar
#CS21C Assignment 2
#This script makes a chart of celsius values 20,40,60,80 with corresponding fahrenheit values
#The equation Fahrenheit = 1.8*celsius +32 is used to calculate fahrenheit



#Prints column labels 
print("Celsius","   Fahrenheit")

#Sets Celsius variable value
celsius = 20

#Sets corresponding Fahrenheit variable with equation F = 1.8*Celsius +32
fahrenheit = float(1.8*celsius + 32)

#Prints Fahrenheit for a specific Celsius
#Formats Celsius as an integer and Fahrenheit as a floating point with 1 decimal
#Also formats the space the Celsius and Fahrenheit numbers take up
print(format(celsius,"4d"), format(fahrenheit,"12.1f"))

#Same process is repeated for C=40,60,80

#Resets Celsius to 40, recalculates Fahrenheit, and prints a line of the table for the Celsius value
celsius = 40
fahrenheit = float(1.8*celsius + 32)
print(format(celsius,"4d"), format(fahrenheit,"12.1f"))

#Resets Celsius to 60, recalculates Fahrenheit,and prints a line of the table for the Celsius value
celsius = 60
fahrenheit = float(1.8*celsius + 32)
print(format(celsius,"4d"), format(fahrenheit,"12.1f"))

#Resets Celsius to 80, recalculates Fahrenheit, and prints a line of the table for the Celsius value
celsius = 80
fahrenheit = float(1.8*celsius + 32)
print(format(celsius,"4d"), format(fahrenheit,"12.1f"))
