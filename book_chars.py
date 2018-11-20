#Ruth Kollar
#CS21
#Assignment 9: book_chars.py
#Asks user for file name and counts the number of uppercase, lowercase, numbers, and spaces, prints results
#uses function character_count to count types of upper,lower,space,digit characters

#main function asks user for file name, then uses character_count function to get values of character counts
#prints results
#uses try/except to catch exception where file does not exist
def main():
    try:
        user_file = input('Enter the filename: ')
        dracula = open(user_file,'r')

        #if file opens, goes on to check text for upper,lower,numbers,spaces
        #if there was an issue opening, script will go to exception
        
        #defines count variables
        upper_total = 0
        lower_total = 0
        space_total = 0
        digit_total = 0
        
        #starts while loop
        line = 'o'
        
        while line != '':
            #reads one line
            line = dracula.readline()

            #character_count function counts upper,lower,space,digit and returns values
            upper, lower, space, digit = character_count(line)

            #runnning count of totals kept
            upper_total += upper
            lower_total += lower
            space_total += space
            digit_total += digit
            
        #prints results
        print('Uppercase Letters: '+format(upper_total,'.0f'))
        print('Lowercase Letters: '+format(lower_total,'.0f'))
        print('Digits: '+format(digit_total,'.0f'))
        print('Spaces: '+format(space_total,'.0f'))

    #exception for file not opening
    except IOError:
        print('Error:  File not found.')
            
        
#function checks each line in the text, counts upper, lower, numbers,spaces
#returns count
def character_count(string):
    #defines variables to use
    upper = 0
    lower = 0
    space = 0
    digit = 0
    #for each character in string, keeps running count of if it's upper,lower,space,or digit
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
    #returns running count
    return upper, lower, space, digit

#calls main
main()
        
        
        
        
