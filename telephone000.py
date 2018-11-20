#Ruth Kollar
#CS21
#Assignment 9: telephone.py
#

#function main prompts user for telephone number
#uses function letter_to_number to convert letters in phone number to numbers
#prints the new phone number
def main():
    user_phone = input('Enter the telephone number in the format XXX-XXX-XXXX: ')
    new_phone = letter_to_number(user_phone)
    print('The phone number is',new_phone)

#function replaces letters in string with numbers
def letter_to_number(string):
    #case insenstiive
    string = string.upper()
    
    #creating alphabet list
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    #creating numbers list
    numbers = []
    for i in range(1,27):
        numbers.append(str(i))

    #for each character in the string, if it is a letter, it's matched to an index in the alphabet list
    #that same index is used to match it to a number, whcih replaces the value in the string
    for i in string:
        if i in alphabet:
            letter_number_index = alphabet.index(i)
            string = string.replace(i, numbers[letter_number_index])

    return string

#calls main
main()
