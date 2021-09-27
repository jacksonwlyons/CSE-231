##############################################################################
#    Computer Project #1
#    
#    Algorithm
#    The goal of this program is to output portage distance
#    input the portage distance in rods 
#
#    The input is then converted to meters, feet, miles, furlongs, minutes 
#    Display input conversions
##############################################################################
#  define input variables
num_str1 = input("Input rods: ")
#  convert input from num_str1 to float  
float1 = float(num_str1)

#  define portage distance variables
meters = (float1 * 5.0292)                   
feet = (meters / 0.3048)
miles = meters / 1609.34
furlongs = float1 / 40
#  minut is a variable for minutes
minut = ((miles / 3.1) * 60)

#  The program prints the input and all the calculations
print("You input",float1,"rods.")
print()
print("Conversions")
print("Meters:",round(meters,3))
print("Feet:",round(feet,3))
print("Miles:",round(miles,3))
print("Furlongs:",round(furlongs,3))
print("Minutes to walk",float1,"rods:",round(minut,3))
#  end of program