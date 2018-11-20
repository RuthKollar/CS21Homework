#Ruth Kollar
#CS21 Assignment 7
#linenumber.py
#This script asks the user for a file and creates a new file that numbers the lines of the user's file
#It uses the function numbering_lines to number the lines


#ask user for the name of the file
def main():
    file_name = input('What is the name of your file? ')

    #opens user's file and opens/creates file that will be the lined version
    user_file = open(file_name, 'r')
    line_file = open('ln_'+file_name, 'a')

    #calls numbering_lines function to number lines
    numbering_lines(user_file,line_file)

    #closes files
    user_file.close()
    line_file.close()

    

#function numbering_lines takes arguments of the opened user file and file to be lined
#it reads the lines of the user file and assigns a line
#then writes the numbered version to the line file
def numbering_lines(user_file, line_file):
    #starts line as something so it's not empty
    line = 'o'
    line_number = 0
    #numbers lines until it hits an empty line
    while line != '':
        line = user_file.readline()
        line = line.rstrip()
        if line != '':
            line_number += 1
            line_file.write(str(line_number)+': '+ str(line)+'\n')


#calls main
main()


