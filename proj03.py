##############################################################################
#    Computer Project #3
#
#    Algortithm
#    input class level
#    Based off class input college
#    Input for admission to James Madison or Engineering
#    Input credits
#    tuition is calculated based off all previous inputs
#    Prompt for continuation
#
##############################################################################



print("2021 MSU Undergraduate Tuition Calculator.\n")

ask = "yes"

#outer while loop to allow continuation if necessary
while ask.lower() == "yes":

    level=str.lower\
        (input("Enter Level as freshman, sophomore, junior, senior: "))
    
    while level != "freshman" and level != "sophomore" and level != "junior" \
        and level != "senior" :
        print("Invalid input. Try again.")
        level = input("Enter Level as freshman, sophomore, junior, senior: ")
        if level == "freshman" or level == "sophomore" or level == "junior" \
            or level == "senior" :
            break
    madison = 0
    college = 0
    egr = 0
    
    #Ask about admission to engineering or if they are in James Madison
    if level == 'junior' or level == 'senior':
        college = input(\
        "Enter college as business, engineering, health, sciences, or none: ")
        if college != "business" and college != "engineering" \
           and college != "health" and college != "sciences" \
           and college != "none":
            madison = input("Are you in the James Madison College (yes/no): ")
    while level == 'freshman' or level == 'sophomore':
        egr = input("Are you admitted to the College of Engineering \
                    (yes/no): ")
        if egr == "yes":
            break
        madison = input("Are you in the James Madison College (yes/no): ")
        if madison == "yes":
            break
        else:
            break
    #These are fees and taxes applicable to all students basically defaults
    fees = 0
    tax = 24
    credits = input("Credits: ")
    
    while credits == "0":
        print("Invalid input. Try again.")
        credits = input("Credits: ")
        if not credits == "0":
            break
    
    
    while credits.isdigit() != True:
        print("Invalid input. Try again.")
        credits = input("Credits: ")
        if credits.isdigit() == True:
            credits = int(credits)
            break
    ##########################################################################
    credits = int(credits)
    
    #Taxes
    if credits >= 6 :
        if madison == "yes":
            tax = tax + 5 + 7.50
        elif madison == "no" :
            tax += 5
        else:
            tax += 5
    
    if credits < 6 :
        if madison == "yes":
            tax += 7.50
    
    #Fees
    if credits <= 4:
        if college == "health" or  college == "sciences" \
        and level == "junior" or level == "senior" : \
            fees = 50
        elif college == "business" and level == "junior" or level == "senior":
            fees = 113
        elif egr == "yes":
            fees = 402
    
    if credits > 4:
        if college == "health" or  college == "sciences":
            if level == "junior" or level == "senior" :
                fees = 100
        elif college == "business":
            if level == "junior" or level == "senior" :
                fees = 226
        elif egr == "yes" or college == "engineering":
            fees = 670
    
    
    ##########################################################################
    
    #Tuition + Taxes + Fees
    if 1 <= credits <= 11:
        if level == "freshman" :
            print("Tuition is ${:,.2f}." .format(482*credits+ (tax + fees)))
        elif level == "sophomore" :
            print("Tuition is ${:,.2f}." .format(494 * credits+ (tax + fees)))
        elif (level == "junior" or level == "senior") \
             and not (college == 'business' or college == 'engineering'):
            print("Tuition is ${:,.2f}." .format(555*credits+ (tax + fees)))
        elif (level == "junior" or level == "senior") \
             and (college == 'business' or college == 'engineering'):
            print("Tuition is ${:,.2f}." .format(573*credits + (tax + fees)))
    
    if 12 <= credits <= 18:
        if level == "freshman" :
            print("Tuition is ${:,.2f}." .format(7230 + (tax + fees)))
        elif level == "sophomore" :
            print("Tuition is ${:,.2f}." .format(7410 + (tax + fees)))
        elif (level == "junior" or level == "senior") \
            and not (college == 'business' or college == 'engineering'):
            print("Tuition is ${:,.2f}." .format(8325 + (tax + fees)))
        elif (level == "junior" or level == "senior") \
            and (college == 'business' or college == 'engineering'):
            print("Tuition is ${:,.2f}." .format(8595 + (tax + fees)))
            
    if credits > 18: 
        if level == "freshman" :
            print("Tuition is ${:,.2f}." .format(7230 + (482*(credits - 18)) \
                  + (tax + fees)))
        elif level == "sophomore" :
            print("Tuition is ${:,.2f}." .format(7410 \
                  + (494 * (credits - 18)) + (tax + fees)))
        elif (level == "junior" or level == "senior") \
            and not (college == 'business' or college == 'engineering'):
            print("Tuition is ${:,.2f}." .format(8325 \
                  + (555 * (credits - 18)) + (tax + fees)))
        elif (level == "junior" or level == "senior") \
            and (college == 'business' or college == 'engineering'):
            print("Tuition is ${:,.2f}." .format(8595 \
                  + (573 * (credits - 18)) + (tax + fees)))
    
    ask = str.lower(input("Do you want to do another calculation (yes/no): "))
