#Ruth Kollar
#CS21C
#Assignment 3: eggs.py
#This script takes user input of number of eggs collected.  It calculates the cartons used to pack the eggs collected and the remainder of eggs.
#EGGS_PER_CARTON = 12, the constant for eggs in each carton
#Equations for calculating cartons used and remaining eggs:
#Cartons = Eggs_Collected // EGGS_PER_CARTON
#Remainder_Eggs = Eggs_Collected % EGGS_PER_CARTON
#Then it prints this information for the user.

#Prints script introduction message and takes user input value of eggs 
#Stores input in Eggs_Collected variable
Eggs_Collected = int(input('This program will determine the required number of 1-dozen egg cartons.  How many eggs did you collect today? '))


#Uses an if clause so that a negative number will not be accepted
#only if the number is positive will it continue with calculations and printing
if Eggs_Collected < 0:
    print('Your value cannot be negative.')
else:
#Sets constant for eggs per carton
    EGGS_PER_CARTON = 12
#Calculates the number of cartons with integer division and stores in Cartons variable
    Cartons = Eggs_Collected // EGGS_PER_CARTON
#Calculates the remainder of eggs with remainder division and stores in Remainder variable
    Remainder_Eggs = Eggs_Collected % EGGS_PER_CARTON

#Prints number of cartons and remainder of eggs
    print('We will pack your', Eggs_Collected, 'eggs in', Cartons, 'cartons.')
    print('There will be', Remainder_Eggs, 'eggs left over.')
