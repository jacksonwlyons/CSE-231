##############################################################################
#    Computer Project #2
#
#    Algortithm
#    Prompt for yes or no
#    input customer code
#    Based off customer code cost is broken down into three options
#    input car information
#    Based off information cost is calculated for the rental
#    Summary of info and costs prints
#    User is prompted for yes or no again
#
##############################################################################


print()
#user start
BANNER = print("Welcome to car rentals.")
print()

print("At the prompts, please enter the following:")
print("        Customer's classification code (a character: BDW)")
print("        Number of days the vehicle was rented (int)")
print("        Odometer reading at the start of the rental period (int)")
print("        Odometer reading at the end of the rental period (int)" )
print()


PROMPT = input("Would you like to continue (Y/N)? ")


while PROMPT == "Y":
    print()
    Class_code = input("Customer code (BDW): ")  
    print()
    
    # Based off customer code, cost is broken down into 3 categories
    while Class_code != 'B' and Class_code != 'D' and Class_code != 'W':
        print("    *** Invalid customer code. Try again. ***")
        print()
        Class_code = input("Customer code (BDW): ")
        if (Class_code == 'B' or Class_code == 'D' or Class_code == 'W'):
            break
    print()
    Days = input("Number of days: ")
    Daysinte = int(Days)
    Start_odom = input("Odometer reading at the start: ")
    # convert odometer inputs to integers for calculations
    Start_odomint = int(Start_odom)
    End_odom = input("Odometer reading at the end:   ")
    End_odomint = int(End_odom)
    mile_charge1 = 0
    import math
    #conditionals and math for varying customer codes
    week = math.ceil(Daysinte / 7)
    if (End_odomint + Start_odomint) > 1000000:
        miles = ((1000000 + End_odomint) - Start_odomint) /10
    elif (End_odomint + Start_odomint) < 1000000:
        miles = (End_odomint - Start_odomint) / 10

    if Class_code == "B":
         cost = (40*Daysinte) + (0.25*miles)
    elif Class_code == "D":
         if (miles/Daysinte) > 100:
            mile_charge1 = (miles - (Daysinte * 100)) /4
    # mile_charge1 is the extra charge for miles over alloted amount
         cost = float((60*Daysinte) + mile_charge1)
    elif Class_code == "W":
         if ((miles/Daysinte) * 7) <= 900:
             mile_charge1 = 0
         elif  900 < ((miles/Daysinte) * 7) < 1500:
             mile_charge1 = 100 * week
         elif ((miles/Daysinte) * 7) > 1500:
             mile_charge1 = (200 * week) + ((miles - (week * 1500))/4) 
         cost = (190 * week)+ mile_charge1
         
    print()
    # customer receipt begins
    print("Customer summary:")
    print("        classification code:", Class_code)
    print("        rental period (days): ", Days)
    print("        odometer reading at start:", Start_odomint - 0)
    print("        odometer reading at end:  ", End_odomint - 0)
    print("        number of miles driven: ", miles)
    print("        amount due: $", (cost + 0.0))        
    print()
    PROMPT = input("Would you like to continue (Y/N)? ") 
             
else:
    print("Thank you for your loyalty.")
print()

