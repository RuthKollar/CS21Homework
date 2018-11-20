#Ruth Kollar
#CS21C Assignment 5
#distance.py
#This script takes user input of the speed of a vehicle in mph and the number of hours it traveled
#It then calculates the distance:
#distance = speed * hours
#And prints the distance the vehicle traveled for each hour of that time period
#the function show_travel is used to collect the time,speed,and to print

#defines main function to collect user input of time and speed
#uses while loop to stop user from continuing if their speed or time<0
#calls show_travel function to uses speed and hours input to print table

def main():
    speed = int(input('Enter the speed of the vehicle in mph: '))
    while speed < 0:
        print('speed must be greater than zero')
        speed = int(input('Enter the speed of the vehicle in mph: '))
        
    hours = int(input('Enter the number of hours traveled: '))
    while hours <= 0:
        print('time must be greater than zero')
        hours = int(input('Enter the number of hours traveled: '))
    show_travel(speed,hours)


#defines function show_travel that uses collected time and speed to print chart
#formats chart from hour 1 to total hours
def show_travel(speed,hours):
    print('Hour  Distance Traveled')
    print('------------------------')
    for hours in range(1,hours+1):
        distance = speed * hours
        print(format(hours,'.0f'),format(distance,'12.1f'))

#calls the main function to take input and run show_travel
main()


