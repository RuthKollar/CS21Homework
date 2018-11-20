#Ruth Kollar
#CS21
#Assignment 8: cities.py
#This script converts vt_municipalities.txt and nh_municipalities.txt into lists and asks the user for a city to compare to the lists
#uses file2list function to convert the text files to lists

#main function asks user for a city name and compares it with the two lists of cities
def main():
    #uses file2list function to convert files to lists and stores returned lists
    vt_list = file2list('vt_municipalities.txt')
    nh_list = file2list('nh_municipalities.txt')

    #define zero constant for empty list
    EMPTY = 0
    
    #if the lists are empty, nothing happens
    #otherwise, the user is prompted for a city name and the city given will be compared to the lists made from files
    if len(vt_list) != EMPTY and len(nh_list) != EMPTY:
        #starts while loop
        city_check = 'o'

        #asks for city name to compare and, as long as user doesn't enter q, keeps asking and checking
        while city_check != 'q':

            city_check = input('City name (type \'q\' to quit): ')
            
            if city_check != 'q':
                #sets variable that marks city match as not a match for default
                in_nh_list = 'n'
                in_vt_list = 'n'
                
                #goes through the vt and nh lists and compares the city check to them
                #if the city matches, variable that marks city match is set to 'y'
                for i in vt_list:
                    if city_check == i:
                        in_vt_list = 'y'
                for i in nh_list:
                    if city_check == i:
                        in_nh_list = 'y'

                #if the city was marked as found in both, either, or neither, the proper result is printed
                if in_vt_list == 'y' and in_nh_list == 'y':
                    print(city_check, 'is in Vermont and New Hampshire.\n')
                elif in_vt_list == 'y':
                    print(city_check, 'is in Vermont.\n')
                elif in_nh_list == 'y':
                    print(city_check, 'is in New Hampshire.\n')
                elif in_vt_list != 'y' and in_nh_list != 'y':
                    print('Neither VT nor NH has a city by that name.\n')
        
    

#defines file2list function which takes file name as argument
#converts the lines of the file to a list and returns the list
#exception handling if file can't be found
def file2list(file_name):
    try:
        #creates city_names_list so it can be appended to
        city_names_list = []
        
        #opens file for reading
        file_object = open(file_name, 'r')
    except IOError:
        print('***FILE ERROR: '+file_name+' cannot be found.')
        return city_names_list
    else:
        
        #starts while loop
        city_line = 'o'
        
        #reads each line of file until the line is empty
        #adds each line to a list
        while city_line != '':
            city_line = file_object.readline()
            #strips newline off
            city_line = city_line.rstrip()
            city_names_list.append(city_line)
                
        #closes file   
        file_object.close()


        #returns list of city names
        return city_names_list

#calls main
main()

    
        
