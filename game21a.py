#Ruth Kollar
#CS21 Assignment 6: game21.py
#This script plays the game of 21 with the user.
#Rules:
    #Each round, the user may roll or not roll
    #The user is informed only of their total sum
    #The game ends if:
        #The user hits or exceeds 21
        #The user chooses not to roll
    #The winner is the first to hit 21 or the highest roll when neither exceeds 21

#This script uses functions:
#main;
    #Uses a while loop and if clauses in the case the user wants to keep rolling so that:
        #User may roll so long as their sum does not meet or exceed 21
        #User and computer rolls are simulated and a total sum is calculated
        #only the user's sum is printed
    #If user stops rolling:
        #the total is summed and winner is based on the highest number
#roll_dice;
    #simulates two die rolling by generating two random numbers between 1 and 6 inclusive
    #outputs two numbers 
#get_response;
    #Asks the user if they want to roll
    #validates input and waits for only 'y' or 'n' as a valid input
    #outputs valid response


#imports random number functionality
import random


#defines main
def main():
    #Starts total user and computer sums at 0
    total_user_sum = 0
    total_computer_sum = 0
    
    #starts while loop
    again = 'y'
    
    #One round of rolling happens each time user says they want to roll
    while again == 'y':
        #checks if user wants to roll again
        again = get_response()

        if again == 'y':
            
            #rolls for the computer and user separately, then stores these rolls as variables 
            computer_die_one, computer_die_two = roll_die()
            user_die_one, user_die_two = roll_die()
            #calculates the sum of the current rolls for user and computer
            current_roll_user_sum = user_die_one + user_die_two
            current_roll_computer_sum = computer_die_one + computer_die_two
            #calculates the total sum from the entire game for user and computer
            total_user_sum += current_roll_user_sum
            total_computer_sum += current_roll_computer_sum
            
            #prints user's total
            print('Points:', total_user_sum)
            
            #If user reaches 21, the game ends
            #And the script displays points and the winner
            if total_user_sum == 21:
                if total_computer_sum == 21:
                    print('User\'s points:', total_user_sum)
                    print('Computer\'s points:', total_computer_sum)
                    print('Tie game!')
                    again = 'c'
                if total_user_sum > total_computer_sum or total_user_sum < total_computer_sum:
                    print('User\'s points:', total_user_sum)
                    print('Computer\'s points:', total_computer_sum)
                    print ('User wins')
                    again = 'c'
                    
            #If user exceeds 21, the game ends
            #The script displays points and the winner
            elif total_user_sum > 21:
                print('User\'s points:', total_user_sum)
                print('Computer\'s points:', total_computer_sum)
                print('Computer wins')
                again = 'c'
        
    #If the user chooses not to roll,
    #The total sum is checked for the winner
    if again == 'n':
        #If the computer and user have the same sum values, they tie
        if total_user_sum == total_computer_sum:
            print('User\'s points:', total_user_sum)
            print('Computer\'s points:', total_computer_sum)
            print ('Tie Game!')
            
        #If computer hit 21, or has a higher sum than user without exceeding 21, the computer wins
        elif total_computer_sum == 21:
            print('User\'s points:', total_user_sum)
            print('Computer\'s points:', total_computer_sum)
            print('Computer wins')

            
       #If user has a higher number than computer or computer exceeded 21, user wins
        elif (total_user_sum > total_computer_sum) or total_computer_sum > 21:
            print('User\'s points:', total_user_sum)
            print('Computer\'s points:', total_computer_sum)
            print('User wins')
        
            
    #if the computer didn't exceed 21 and has a higher number than the user, the computer wins
        elif total_user_sum < total_computer_sum and total_computer_sum < 21:
            print('User\'s points:', total_user_sum)
            print('Computer\'s points:', total_computer_sum)
            print('Computer wins')



#defines roll dice function
def roll_die():
    first_die = random.randint(1,6)
    second_die = random.randint(1,6)
    return first_die,second_die


#defines get response function
#only accepts 'y' or 'n'
def get_response():
    response = input('Do you want to roll? ')
    while response != 'y' and response != 'n':
        response = input('Please enter \'y\' or \'n\' ')
    return response


#runs main
main()

        
