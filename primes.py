#Ruth Kollar
#CS21C Assignment4
#primes.py
#This script prompts the user for an integer >1 and uses a while loop to check that the value is >1 before letting the user continue.
#Then the script checks if the number is prime and prints the result.
#It then asks if the user would like to continue.
#Uses for loop to test if number is divisible by all numbers from 2 to number-1

#Introduction to script
print('Welcome to my prime number detector.')
print('Provide an integer and I will determine if it is prime.')

#sets try_again as 'y' so if clause will run
try_again = 'y'

while try_again == 'Y' or try_again == 'y':
    #resets prime value
    prime = 1
    #asks the user for integer >1
    number = int(input('Enter an integer > 1: '))
    
    #checks the number is >1, won't progress until number>1
    while number <= 1:
        number = int(input('Input must be > 1, try again: '))

    #tests if the number is prime
    #If the number is prime there will be a remainder for all numbers not 1 and the number itself
    for divisor in range(2,(number-1)):
        prime_check = number%divisor
        #scripts 'assumes' number is prime, with prime = 1
        #As long as there is one number in the range checked that divides without remainder into the number
        #It is not prime, so the prime value goes to prime = 0 to show it's not prime
        if prime_check == 0:
            prime = 0
        
    #prints whether the number is prime or not        
    if prime == 1:
        print(number, 'is prime.')
    elif prime ==0:
        print(number, 'is not prime.')
        
    #asks if the user wants to continue and stores answer as continue variable
    try_again = input('Do you want to try another number? (Y/N): ')

