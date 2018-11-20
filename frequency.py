#Ruth Kollar
#CS21
#Assignment 10:frequency.py
#This script asks user for a filename and counts the frequency of words in the file
#It then displays the frequencies as a histogram
#uses function create_word_count_dictionary to count word frequencies

#Function asks user for filename and counts frequency of words in file, displays histogram of frequencies
def main():
    
    #try/except for error in opening file
    try:
        
        #prompts user for file name
        user_file = input('Enter the filename: ')
        #opens file for reading
        file_object = open(user_file,'r')

        #creates punctuation list to replace punctuation
        #creates word list to add words to
        punctuation = '\'\"\\?,.;:!'
        word_list = []

        #nonempty line to start while loop
        line = 'uwu'
    
        
        #reads line until there aren't any lines left
        #each line is split into words, which are appended to a word list
        while line!= '':
            #reads each line
            line = file_object.readline()
            #case insensitive
            line = line.lower()
            #strips trailing white space
            line = line.rstrip()

            #replaces all punctuation with white space and splits by white space
            for ch in punctuation:
                line = line.replace(ch,' ')
                
            #saves split list into line_split_list variable
            line_split_list = line.split()
 
            #each word is appended to the list word_list
            for word in line_split_list:
                word_list.append(word)
                       
        #creating word counter variable and word count dictionary to append to
        word_count = 0
        word_count_dictionary = {}
        
        #calls create_word_count_dictionary function to create word_count_dictionary
        word_count_dictionary = create_word_count_dictionary(word_list)


        #prints header and dash line
        print('\nWord Frequency')
        print('  --------------')
                       
        #for every key/value pair, the histogram_maker function prints a line of histogram
        for key in word_count_dictionary:
            print('  '+key + ': ' + '*' * word_count_dictionary[key])

        #closes user's file
        file_object.close()
                       
    #Error in opening file exception               
    except IOError:
        print('Error opening file.')



#function takes list of all words and counts each word, adding the word and count to word_count_dictionary
def create_word_count_dictionary(word_list):
    #list to remove words from so word_list in for loop isn't affected
    word_list_remove = []+word_list
    
    #creates empty word count dictionary
    word_count_dictionary = {}
    
    #for each word, it is counted and removed until all occurrences have been removed
    for word in word_list:
        
        #if the word hasn't already been counted, it counts by removing
        if word not in word_count_dictionary:
            #sets counter to zero
            word_count = 0
            
            while word in word_list_remove:
                word_list_remove.remove(word)
                #adds to counter every time it removes the word
                word_count += 1
                
            #then the count and the word are added to the word count dictionary as value and key
            word_count_dictionary[word] = word_count

    #returns the dictionary
    return word_count_dictionary
    

#calls main
main()    
    
        
