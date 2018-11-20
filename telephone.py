#Ruth Kollar
#CS21
#Assignment 9: telephone.py
#script converts letters in phone number to numbers according to phone keypad conversion
#uses function letter_to_number to convert letters to numbers

#function main prompts user for telephone number, uses function letter_to_number to convert letters in phone number to numbers
#assigns number to letter's position and prints the new phone number
def main():

    try:
        
        #prompt user for phone number 
        user_phone = input('Enter the telephone number in the format XXX-XXX-XXXX: ')

        #for each character, if that character is a letter, the function letter_to_number assigns a number
        #the number replaces the letter
        for char in user_phone:
            if char.isalpha():
                new_char = str(letter_to_number(char))
                #replaces letter character with number character
                user_phone = user_phone.replace(char,new_char)
                
        #prints number       
        print('The phone number is',user_phone)

    #general exception 
    except:
        print('An error occurred.')


#function converts letters to numbers and returns number value
def letter_to_number(letter):
    #case insenstiive
    letter = letter.upper()

    #assigns number value
    if letter == 'A' or letter == 'B' or letter == 'C':
        number = 2
    if letter == 'D' or letter == 'E' or letter == 'F':
        number = 3
    if letter == 'G' or letter == 'H' or letter == 'I':
        number = 4
    if letter == 'J' or letter == 'K' or letter == 'L':
        number = 5
    if letter == 'M' or letter == 'N' or letter == 'O':
        number = 6        
    if letter == 'P' or letter == 'Q' or letter == 'R' or letter == 'S':
        number = 7
    if letter == 'T' or letter == 'U' or letter == 'V':
        number = 8
    if letter == 'W' or letter == 'X' or letter == 'Y' or letter == 'Z':
        number = 9        
    #returns number value
    return number

#calls main
main()
