#Ruth Kollar
#CS21
#Assignment 9: msg_chars.py
#This script counts how many of each kind of letter are in a string and is case-insensitive.  Then prints a table.
#uses function count_letter to count occurrences of letters in string

#main function asks user for a string, uses count_letter function to count how many times a character appears
#Then prints a table for the values
def main():

    try:
        #takes user input of a string
        user_string = input('Enter a string: ')

        #case insensitive
        user_string = user_string.upper()
        
        #creates a list of non-repeating characters and letter occurrences
        non_repeating_list = []
        occurrences_list = []
        user_list = []

        #creates a list of all the elements of the string, including repeats
        for letter in user_string:
            user_list += letter
            
        #creates a list of all the elements of the string, excluding repeats
        for letter in user_string:
            if letter not in non_repeating_list:
                non_repeating_list.append(letter)
                
        #for every non-repeated element of the string,
        #the function count_letter is used to find how many times it occurs in the list made from the user's string     
        for letter in non_repeating_list:
            occurrences_list.append(count_letter(letter,user_list))

        #prints table header
        print('Letter'+'\t'+'Freq')
        
        #prints table values
        for i in range(0,len(non_repeating_list)):
            print('  '+non_repeating_list[i],format(occurrences_list[i],'6.0f'))
            
    #general exception statement
    except:
        print('An error occurred.')
        
        

#function takes a letter and the user string as input and counts occurrences by finding and removing letter from user_string until all letter have been found
def count_letter(letter,user_list):
    #defining variables and starting while loop
    occurrence = 0
    letter_index = 0
    #as long as the letter is in the user_list, it will be removed and counted
    while letter in user_list:
        user_list.remove(letter)
        occurrence += 1
    #returns how many times letter occurred    
    return occurrence

#calls main
main()

