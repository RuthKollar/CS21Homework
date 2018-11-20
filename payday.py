#Ruth Kollar
#CS21
#Assignment 8: payday.py
#This script takes user input for names, hours worked, and hourly rate, and calculates the total payroll, total earned for each person, and average paycheck
#It writes this information to a file called payroll.txt

    
#function main asks takes user input for name, hours worked, and hourly rate, then adds these to a list
#uses exception handling to make sure only numbers are entered
def main():
    
    #creates name,hours,and hourly rate list
    name_list = []
    hours_list = []
    hourly_rate_list = []

    #starts while loop
    name = 'o'
    
    #stops asking for names when the user just hits enter
    #Exception handling for the user not entering numbers for the hours worked/hourly rate
    while name!='':
        name = input('Name (just hit Enter when done): ')
        if name != '':
            #appends user input to lists
            #tries to convert input to float, but has exception handling if user doesn't enter numbers
            try:
                hours = float(input('Hours worked: '))
                hourly_rate = float(input('Hourly rate: '))
                name_list.append(name)
                hours_list.append(hours)
                hourly_rate_list.append(hourly_rate)
            except ValueError:
                print('Values must be numeric.')
                print('Please input employee\'s name and values again.')
                    

    #calls function to create payroll test
    create_payroll_text(name_list,hours_list,hourly_rate_list)


#function takes the name, hours, and hourly rate list created in main as arguments
#calculates the total pay per person, total payroll, average paycheck, and writes information to payroll.txt file
def create_payroll_text(name_list,hours_list,hourly_rate_list):
    #opens payroll.txt file
    payroll = open('payroll.txt','w')
    total_payroll = 0
    #for each person: calculates total pay per person and adds pay to running total
    #writes information to line in payroll file
    for i in range(0,len(name_list)):
        total_pay_person = hours_list[i]*hourly_rate_list[i]
        total_payroll += total_pay_person
        payroll.write(name_list[i]+'\t'+' '*4+ format(hours_list[i],'.2f')+' '+ format(hourly_rate_list[i],'.2f') +' ' + format(total_pay_person,'.2f')+'\n')

    #after going through each person's data, calculates average and writes total payroll and average to payroll file
    average_paycheck = total_payroll/len(name_list)
    payroll.write('\n'+'Total Payroll = $'+ format(total_payroll,'.2f')+ '\n' + 'Average Paycheck = $' + format(average_paycheck,'.2f'))

    #closes payroll file 
    payroll.close()


#calls main
main()
        

    
