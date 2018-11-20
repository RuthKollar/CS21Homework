#Ruth Kollar
#CS21C
#Assignment 3: biggest_num.py
#This program asks the user for three integers, then displays them in descending order
#It uses if statements to check how large the numbers are in comparison to the other numbers.  Then it assigns them a value of Largest, Middle, or Smallest
#and print them in descending order.

#Asks user input for first number and stores in integer variable (First_Num)
First_Num = int(input('First Number? '))

#Asks user input for second number and stores in integer variable (Second_Num)
Second_Num = int(input('Second Number? '))

#Asks user input for third number and stores in integer variable (Third_Num)
Third_Num = int(input('Third Number? '))


#These if statements check for any numbers given being equal
#If they are all equal, it doesn't matter what order they're in
#So they're just assigned variables to print
if First_Num == (Second_Num and Third_Num):
    Smallest = First_Num
    Middle = Second_Num
    Largest = Third_Num


#After checking that all three are not equal
#The script uses if statements to check for two being equal in the three combinations possible
#If two numbers are equal, their relation to the third number is checked using an if statement
#to determine whether the equivalent numbers are larger or smaller
#Then the numbers are assigned Largest, Middle, or Smallest values for printing

if First_Num == Second_Num:
    if First_Num > Third_Num:
        Largest = First_Num
        Middle = Second_Num
        Smallest = Third_Num

    elif First_Num < Third_Num:
        Largest = Third_Num
        Middle = Second_Num
        Smallest = First_Num


if Second_Num == Third_Num:
    if Second_Num > First_Num:
        Smallest = First_Num
        Middle = Second_Num
        Largest = Third_Num
    elif Second_Num < First_Num:
        Smallest = Third_Num
        Middle = Second_Num
        Largest = First_Num
    
if First_Num == Third_Num:
    if First_Num > Second_Num:
        Largest = First_Num
        Smallest = Second_Num
        Middle = Third_Num
    elif First_Num < Second_Num:
        Middle = Third_Num
        Largest = Second_Num
        Smallest = First_Num
    


#The tier of if statements checks the First_Num for being the largest number, then the middle number.
#If neither of these are true, then First_Num must be the smallest
#Within each outcome of First_Num being Largest, Middle, or Smallest, 
#the script checks the Second_Num in comparison to Third_Num in order to assign it one of the leftover two ranks
#Ranks are recorded by setting variables Largest, Middle, or Smallest equal to the numbers
        
#If First_Num is the larger than both of the others, it is the largest
if First_Num > Second_Num and First_Num > Third_Num:
    Largest = First_Num
    if Second_Num > Third_Num:
        Middle = Second_Num
        Smallest = Third_Num
    elif Second_Num < Third_Num:
        Smallest = Second_Num
        Middle = Third_Num
        
#If First_Num is not the largest, but is still bigger than one of the numbers,
#it must be in the middle
elif First_Num > Second_Num or First_Num > Third_Num:
    Middle = First_Num
    if Second_Num > First_Num:
        Largest = Second_Num
        Smallest = Third_Num
    elif Second_Num < First_Num:
        Smallest = Second_Num 
        Largest = Third_Num 
        
#Otherwise, it must be the smallest        
elif First_Num < Second_Num and First_Num < Third_Num:
    Smallest = First_Num
    if Second_Num > Third_Num:
        Largest = Second_Num
        Middle = Third_Num 
    elif Second_Num < Third_Num:
        Middle = Second_Num 
        Largest = Third_Num
        
    

#Prints the numbers in descending order
print('Descending order: ' ,Largest, Middle, Smallest)
