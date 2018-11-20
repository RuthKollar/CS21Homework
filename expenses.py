#Ruth Kollar
#CS21 Assignment 6: expenses.py
#This script calculates the total cost of gasoline
#It uses functions:
#main; takes user input of total miles driven and percent of total miles driven on the highway
    #converts entries to floats
    #uses while loop to validate miles driven >0; and percent highway betwen 0 and 100
    #uses while loop ask user if they want to run the script again
#total_gallons; this takes input of total miles and highway percentage
    #calculates total_highway_miles and total_city_miles using:
    #total_highway_miles = user_total_miles_driven * (highway_percentage/MAKE_PERCENT_DECIMAL)
    #total_city_miles = user_total_miles_driven - total_highway_miles
    #where constant MAKE_PERCENT_DECIMAL = 100
    #Then uses it computes total gas consumption using:
    #total_gas_consumption = total_highway_miles/MPG_HWY + total_city_miles/MPG_CITY
    #where constants MPG_HWY = 38 and MPG_CITY = 28
    #returns total_gas_consumption
#gas_expense; this takes input of total gallons used
    #and computes the total spent gasoline on the trip
    #total_spent = PRICE_PER_GALLON * total_gallons
    #where constant PRICE_PER_GALLON = 2.29
    #returns total_spent

#defining constants
MPG_CITY = 28
MPG_HWY = 38
PRICE_PER_GALLON = 2.29
MAKE_PERCENT_DECIMAL = 100



#Introduction to the script
print('Computing your gasoline expenses...')

#defines main function, which takes total miles driven and highway percentage as input
#uses while loop to validate input of positive miles driven and 0-100 value of highway percentage
def main():
    #variable to allow while loop beginning
    again = 'y'
    
    while again == 'y' or again == 'Y':
        #takes user input and validates it
        user_total_miles_driven = float(input('\nTotal miles driven: '))
        while user_total_miles_driven < 0:
            user_total_miles_driven = float(input('Enter a value > 0: '))
            
        user_highway_percentage = float(input('Percentage of total miles driven on highway: '))
        while user_highway_percentage < 0 or user_highway_percentage > 100:
            user_highway_percentage = float(input('Enter a value between 0 and 100: '))

        #uses user input of total_gallons to compute and output gas consumption and store in variable
        gas_consumption = total_gallons(user_total_miles_driven,user_highway_percentage)
        #uses calculated gas consumption to compute and output the total spent on gas and store in variable
        total_spent = gas_expense(gas_consumption)

        #prints total miles, gas consumption, total cost
        print('\nHere is the information for your trip:\n')
        print('Total miles: ',format(user_total_miles_driven,'.1f'))
        print('Gas consumption: ', format(gas_consumption, '.1f'), 'gal')
        print('Total cost: $', format(total_spent, '.2f'))

        #asks if user wants to continue
        again =  input('\nCompute gas expense for another trip (y or n)? ')
            
#defines total_gallons function
def total_gallons(user_total_miles_driven,user_highway_percentage):
        total_highway_miles = user_total_miles_driven * (user_highway_percentage/MAKE_PERCENT_DECIMAL)
        total_city_miles = user_total_miles_driven - total_highway_miles
        total_gas_consumption = total_highway_miles/MPG_HWY + total_city_miles/MPG_CITY
        return total_gas_consumption
    
#defines gas_expense function
def gas_expense(total_gallons):
    total_spent = total_gallons * PRICE_PER_GALLON
    return total_spent

#runs main
main()
    


