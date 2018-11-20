#Ruth Kollar
#CS21C
#Assignment 3: mass_weight.py
#This script takes user input for an object's mass in Kg
#Then it calculates the object's weight in Newtons using:
#GRAVITY = 9.8 , the gravity constant
#Weight = Mass * GRAVITY
#The script will print the weight of the object and whether the object is:
    #Too heavy if the object weighs more than 500 newtons
    #Too light if the objects weighs less than 100 newtons

#Setting gravity constant 9.8
GRAVITY = 9.8
#Stores user entry of mass (in kilograms) in variable Mass.
Mass = float(input('Enter the object\'s mass in kilograms: '))

#if statement checks that the given mass is positive 
if Mass < 0:
    print('Mass must be >=0')
#Only if the mass is positive does it proceed to calculations
#if not, the message is printed and nothing more happens
else:
    #Calculates weight and stores in Weight variable
    Weight = Mass * GRAVITY
    #Prints the object's weight.
    print('Object weight:',format(Weight, '.2f'))
    #Uses if statement to check if weight>500 or <100
    #Prints message if either of these is true
    if Weight > 500:
        print('The object is too heavy.  It weighs more than 500 Newtons.')
    elif Weight <100:
        print('The object is too light.  It weighs less than 100 Newtons.')
    
    
        
             
