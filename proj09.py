##############################################################################
#    Computer Project #9
#
#    Algortithm
#    Open a file for reading based on user input
#    Build a dictionary containing different foods, ingredients, etc from 
#    different regions and states
#    Input a list of foods and get the ingredients required to make the food
#    Input a list of ingredients and get the foods you can make
#    Input foods and ingredients, useful and missing ingredients are returned
#    Input foods and preferences, return only foods specified in preferences
#    User can quit to end program
#
##############################################################################

import csv

def open_file(s):
    '''This function opens a file based on user input for reading'''
    while True: 
        x = input('Input a {} file: '.format(s))
        try:
            fp = open(x, 'r')

            return fp
        except  FileNotFoundError:
            print("Invalid filename, please try again.")
            
def build_dictionary(fp):
    ''' This function accepts the previously generated file pointer as \
        input and returns the required dictionary '''
    superD = {}
    reader = csv.reader(fp) # set up the reader
    header = next(reader,None) # skip 1 lines
    for line in reader: # loop through the file
        if '-1' in line:  #If a line contains a '-1' ignore that line
            continue
        food_list = []
        food_name = line[0]
        food_name = food_name.strip()
        ingred = line[1]
        ingred = ingred.lower()
        ingred = ingred.strip()
        ingred = ingred.split(',')
        count = -1
        for item in ingred:
            count+=1
            ingred[count] = item.strip() #strip spaces from ingredients
        ingred = set(ingred)
        food_list.append(ingred)
        diet = line[2]
        food_list.append(diet)
        prep = int(line[3])
        cooking = int(line[4])
        food_tup = (prep, cooking)
        food_list.append(food_tup)
        flavor = line[5]
        food_list.append(flavor)
        state = line[7]
        region = line[8]
        #The following if statements look for repeated state, 
        # region or food names
        if region not in superD:
            superD[region] = {state:{food_name:food_list}}
        elif state not in superD[region]:
            superD[region][state] = {food_name:food_list}
        elif food_name not in superD[region][state]:
            superD[region][state][food_name] = food_list
        
    return superD
        
def get_ingredients(superD,L):
    ''' This function takes in a list of food names and a dictionary, \
        and returns a set of ingredients that are \
            required to make these foods '''
    ingred_set = set()
    L = [food_name.strip() for food_name in L]       
    for region in superD:                  #Iterate through superD
        for state in superD[region]:
            for food_name, value in superD[region][state].items():
                if food_name in L:
                    for items in value[0]:
                        ingred_set.add(items)
    
    return ingred_set
                    
def get_useful_and_missing_ingredients(superD, foods, pantry):
    ''' This function takes 3 parameters: the dictionary superD, a list of \
        foods you want to make, and a list of ingredients that you currently \
            have. The function returns a tuple of two lists:\
                useful ingredients and missing ingredients '''
    x = get_ingredients(superD, foods)  #use get_ingredients function to iterate through superD, 
    missing_ingred = x.difference(set(pantry))   #and identify necessary ingredients based on foods parameter
    useful_ingred = x.intersection(set(pantry))
    useful_ingred = sorted(useful_ingred)
    missing_ingred = sorted(missing_ingred)
    miss_use_tup = (useful_ingred, missing_ingred)
    return miss_use_tup

def get_list_of_foods(superD, pantry):
    ''' This function takes in a list of ingredients as a parameter and \
        the nested super dictionary superD. It then return a list of all \
            possible foods that can be made given the ingredients '''
    result_foods = []
    possible_foods = []
    for region in superD:
        for state in superD[region]:
            for food_name, value in superD[region][state].items():
                #print(food_name, set(pantry).issuperset(value[0]), value)  #[0]
                if set(pantry).issuperset(value[0]):    #compare pantry set to ingredients set in superD
                    possible_foods.append((sum(value[2]), food_name))
    possible_foods = sorted(possible_foods)
    #print(possible_foods) 
    for item in possible_foods:
        result_foods.append(item[1])   #new list
    #print(result_foods)
    return result_foods
        
def get_food_by_preference(superD, preferences):
    ''' This function takes in the super dictionary and a list of \
    preferences as parameters. It then returns a list of foods which match \
    the conditions listed in the list of preferences sorted alphabetically '''
    pref_list = []
    for region in superD:
        if preferences[0] is None or region == preferences[0]:
            for state in superD[region]:
                if preferences[1] is None or state == preferences[1]:
                    for food in superD[region][state]: #[state][food] -> a list where you get vegetarian preference at index 1.
                        if (preferences[2] is None or superD[region][state][food][1] == preferences[2]) and (preferences[3] is None or superD[region][state][food][-1] == preferences[3]):   #food represent the key ('food') 
                            pref_list.append(food)
    pref_list = sorted(pref_list)
    return pref_list
    
def main():  
    print("Indian Foods & Ingredients.\n")
    x = open_file('indian_food')
    superD = build_dictionary(x)
                  
    MENU = '''
        A. Input various foods and get the ingredients needed to make them!
        B. Input various ingredients and get all the foods you can make with them!
        C. Input various foods and ingredients and get the useful and missing ingredients!
        D. Input various foods and preferences and get only the foods specified by your preference!
        Q. Quit
        : '''
    menu_in = input(MENU).upper()
    #start of if statements for menu choices
    while True:
        if menu_in.upper() != 'A' and menu_in.upper() != 'B' and menu_in.upper() != 'C' and menu_in.upper() \
            != 'D' and menu_in.upper() != 'Q':
                print("Invalid input. Please enter a valid input (A-D, Q)")
            
        if menu_in.upper() == 'A':
            foods_list = input('Enter foods, separated by commas: ')
            foods_list = foods_list.split(',')
            ingredients = get_ingredients(superD, foods_list)
            ingredients = sorted(ingredients)
            print('Ingredients: ')
            print(*ingredients, sep=", ", end=" ")
        if menu_in.upper() == 'B':
            ingred_list = input('Enter ingredients, separated by commas: ')
            ingred_list = ingred_list.split(',')
            for i in range(len(ingred_list)): #loop through items in list, strip spaces
                ingred_list[i] = ingred_list[i].strip()
            possible_foods = get_list_of_foods(superD, ingred_list)
            print('Foods: ')
            print(*possible_foods, sep=", ", end=" ")
        if menu_in.upper() == 'C':
            foods_list = input('Enter foods, separated by commas: ')
            ingred_list = input('Enter ingredients, separated by commas: ')
            foods_list = foods_list.split(',')
            ingred_list = ingred_list.split(',')
            for i in range(len(ingred_list)):
                ingred_list[i] = ingred_list[i].strip()
            for i in range(len(foods_list)):
                foods_list[i] = foods_list[i].strip()
            use, miss = get_useful_and_missing_ingredients(superD, foods_list, ingred_list)
            print('Useful Ingredients: ')
            print(*use, sep=", ", end=" ")
            print('Missing Ingredients: ')
            print(*miss, sep=", ", end=" ")
        if menu_in.upper() == 'D':
            preferences = input('Enter preferences, separated by commas: ')
            preferences = preferences.split(',')
            for i in range(len(preferences)):
                preferences[i] = preferences[i].strip()
            food_prep = get_food_by_preference(superD, preferences)
            print('Preferred Food: ')
            print(*food_prep, sep=", ", end=" ")
        
        if menu_in.upper() == 'Q':
            break
        menu_in = input(MENU)
    print("Thanks for playing!")        

if __name__ == '__main__':
    main()

#end           