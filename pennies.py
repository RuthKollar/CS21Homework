#Ruth Kollar
#CS21C Assignment 4
#pennies.py
#This script calculates the how much a person would earn over a period of time
#if their salary is 0.01 on day 1, 0.02 day 2, and so on.
#It shows these values in a table of all the days.
#Uses equations:
#daily_salary = 0.01 * 2**(day-1)
#average_daily_wage = sum_days/number_days
#It also displays average daily wage and total earned, which is calculated
#in the same for loop that creates the table using an augmented operator

#asks for user input of number of days worked
number_days = int(input('Number of days worked: '))

#Won't let user continue until number of days is >=1
while number_days <= 0:
    number_days = int(input('Enter number of days >= 1: '))

#defines sum_days so it exists for 'for' loop
sum_days = 0

#Prints header for table
print('\nSalary Earned Each Day\n')
print(' Day \t Amount ($)')
print(' ---     ----------')

#Calculates the salary of each day and adds all the days
#Uses for loop to calculate the daily_salary for money made each day
#then adds each daily salary for every day worked
#prints a line of the table for each day
for day in range(1,number_days+1):
    #calculation for that day
    daily_salary = 0.01 * 2**(day-1)
    #sum_days is added to with each daily_salary calculated
    sum_days += daily_salary
    print(format(day, '3.0f'), format(daily_salary, '12.2f'))

#prints total pay
print('\nYour total pay = $',end = '')
print(format(sum_days, '.2f'))

#calculates and prints average daily wage
average_daily_wage = sum_days/number_days
print('Your average daily wage = $',end = '')
print(format(average_daily_wage, '.2f'))
    
