#Ruth Kollar
#CS21 Assignment 7: kinetic.py
#script takes user's inputs of mass and velocity
#uses kinetic_energy function to calculate
#function kinetic_energy takes arguments of object's mass in kg and velocity in m/s 
    #returns kinetic energy, using equation:
    #kinetic_energy = KINETIC_ENERGY_CONSTANT * mass * velocity**SQUARED_CONSTANT
    #KINETIC_ENERGY_CONSTANT = 0.5
    #SQUARED_CONSTANT = 2

#defines constant
KINETIC_ENERGY_CONSTANT = 0.5
SQUARED_CONSTANT = 2
#main asks user for mass and velocity
#then uses kinetic_energy function to calculate kinetic energy
#except statement tells user they have to enter numbers if they enter letters
#if there's no problem with user input, main prints the kinetic energy
def main():
    #starts while loop
    again = 1
    #keeps going until the kinetic energy can be calculated
    while again == 1:
        try:
            mass = float(input('Enter the mass in kg: '))
            velocity = float(input('Enter the velocity in m/s: '))
            kinetic_energy = calculate_kinetic_energy(mass,velocity)
        except ValueError:
            print('The mass and velocity must be numbers.')
        else:
            print('The kinetic energy is',format(kinetic_energy,'.2f'))
            again = 0

#function calculates kinetic energy from mass and velocity
#returns kinetic energy value
def calculate_kinetic_energy(mass,velocity):
    kinetic_energy = KINETIC_ENERGY_CONSTANT * mass * velocity**SQUARED_CONSTANT
    return kinetic_energy


main()
