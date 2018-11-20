#Ruth Kollar
#CS21 Assignment 7
#grades.py
#This script uses the grades.txt file and creates a grades_out file
#that lists the numerical scores for the grades and includes a histogram
#made with asterisks
#FileNotFoundError and ValueError are checked by exceptions
#and the user is told what went wrong
#If ValueError occurs, the grades_out file will be completed,
#but without the lines that caused the error

#Grade cutoff constants
A_CUTOFF = 90
B_CUTOFF = 80
C_CUTOFF = 70
D_CUTOFF = 60
F_CUTOFF = 50

#defines grades variables
A = 0
B = 0
C = 0
D = 0
F = 0



#main function uses try/except to open grades, exception handling for the file not being found
#uses try/except to read each line of the grades text, exception handling for non-number lines
#assigns a letter score and counts the number of times a letter is assigned, writes letter to outfile
#uses grade_asterisk function to write lines of histogram for each score
def main():
    try:
        grade_list = open('grades.txt','r')
        grades_out = open('grades_out.txt','a')
    #If there's a FileNotFound error, user will be told to move file
    except FileNotFoundError:
        print('The grades.txt file is not in the same folder as the python file or does not exist.\nThey must be in the same folder for the program to find grades.txt')
    else:
        #defines grades variables
        A = 0
        B = 0
        C = 0
        D = 0
        F = 0
        #defines line variable
        score = 'o'
        #keeps reading grades until there's nothing in the line
        #counts number of grades
        while score != '':
            try:
                score = grade_list.readline()
                if score != '':
                    score = int(score.rstrip())
                    if score >=A_CUTOFF:
                        letter_score = 'A'
                        A+=1
                    elif score >= B_CUTOFF:
                        letter_score = 'B'
                        B+=1
                    elif score >= C_CUTOFF:
                        letter_score = 'C'
                        C+=1
                    elif score >= D_CUTOFF:
                        letter_score = 'D'
                        D+=1
                    elif score >= F_CUTOFF:
                        letter_score = 'F'
                        F+=1
                    score = str(score)
                    grades_out.write(str(letter_score) +'\n')
            
            #if there's a line that can't be converted to an integer, ValueError exception will tell user
            except ValueError:
                print('There was at least one non-number in the grades file.')
                print('Any non-number lines were skipped.')
                print('The rest of the grades were printed and added to the histogram.')
                

                
        #adds new line between grades and histogram
        grades_out.write('\n')

        #grade_asterisk function writes asterisk histogram for all grades
        grades_out.write(grade_asterisk(A,'A'))
        grades_out.write(grade_asterisk(B,'B'))
        grades_out.write(grade_asterisk(C,'C'))
        grades_out.write(grade_asterisk(D,'D'))
        grades_out.write(grade_asterisk(F,'F'))

        #closes files
        grade_list.close()
        grades_out.close()


#function writes line of the histogram
#takes arguments of the numerical grade and the string name for the grade
def grade_asterisk(grade, stringgrade):
    histogram_line = stringgrade +': '+ grade * '*'+'\n'
    return histogram_line

#calls main
main()


    


    

    
