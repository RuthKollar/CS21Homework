#Ruth Kollar
#CS21C Assignment 5
#taxes.py
#This script takes user input of the actual value of a piece of property
#It then calculates and displays the assessment value and property tax
#Equations and constants used:
#assessment_value = 0.60 * actual_value
#where ASSESSMENT_PERCENT = 0.60
#
#property_tax = (assessment_value)/100 * 0.72
#where HUNDRED_IN_PROPERTY_TAX = 100
#and PROPERTY_TAX_CENTS = 0.72
#function main() takes input and calculates

#defines constants used in equations
ASSESSMENT_PERCENT = 0.60
HUNDRED_IN_PROPERTY_TAX = 100
PROPERTY_TAX_CENTS = 0.72

#defines main function
#function main() takes input of actual value
#will not continue until user enters actual value >0
#calculates assessed value and property tax, then calls show_property_tax function
def main():
    actual_value = float(input('Enter the actual value: '))
    while actual_value < 0:
        print("Actual value must be >=0")
        actual_value = float(input('Enter the actual value: '))
        
    assessment_value = ASSESSMENT_PERCENT * actual_value
    property_tax = (assessment_value)/HUNDRED_IN_PROPERTY_TAX * PROPERTY_TAX_CENTS

    show_property_tax(assessment_value,property_tax)

    
#defines show_property_tax function
#takes assessment_value and property_tax as arguments, then
#function show_property_tax formats and prints 
def show_property_tax(assessment_value,property_tax):
    print('Assessed value: $', end = "")
    print(format(assessment_value ,',.2f'))
    print('Property tax: $', end = "")
    print(format(property_tax,',.2f'))


#calls main function
main()


    
