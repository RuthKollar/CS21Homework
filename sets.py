#Ruth Kollar
#CS21
#Assignment 10: sets.py
#Script compares the words in two user-given text files
#Prints the union, intersection, difference (both ways), and symmetric difference
#uses function file_to_set to convert files into sets

#function converts files to sets and prints union, intersection,difference,symmetric difference
def main():
    try:
        #takes user input for files
        file_name1 = input('Enter the name of the first file: ')
        file_name2 = input('Enter the name of the second file: ')

        #uses file_to_set function to convert files to sets
        set1 = file_to_set(file_name1)
        set2 = file_to_set(file_name2)

        if set1 != '' and set2 != '':
            
            #prints text describing what elements are being printed
            #prints elements of specified relation
            print('\nUnion: All unique words in both files:')
            for i in (set1|set2):
                print(i)

            print('\nIntersection: Words in both files:')
            for i in (set1 & set2):
                print(i)

            print('\nDifference: Words in file 1, but not file 2:')
            for i in  (set1-set2):
                print(i)

            print('\nDifference: Words in file 2, but not file 1:')
            for i in (set2-set1):
                print(i)

            print('\nSymmetric Difference: Words in file 1 or file 2, but not in both file 1 and 2:')
            for i in (set1^set2):
                print(i)

    #general exception 
    except Error:
        print('An error occurred.')


#function converts the files given by file names to sets
#returns set
#exception handling if file cannot be opened
def file_to_set(file_name):
    try:
        #opens file name
        file = open(file_name,'r')
        #creates empty set to add to
        file_set = set('')
        #creates punctuation string to use later to replace with spaces
        punctuation = '.,:;!?\\\'\"'

        #line defined for while loop
        line = 'uwu'
        
        #reads lines of the file and adds each word to a set
        while line != '':
            #reads in line 
            line = file.readline()
            #strips trailing white space
            line = line.rstrip()
            #case insensitive
            line = line.lower()

            #replaces punctuation with white space
            for ch in punctuation:
                line = line.replace(ch,' ')
            #splits by white space    
            line_list = line.split()

            #adds words to set
            for word in line_list:
                file_set.add(word)
                
        #returns file set        
        return file_set
    
    #exception for error in file opening
    except IOError:
        print('An error occurred.  File', file_name,'could not be opened.')
        return ''

#calls main
main()





