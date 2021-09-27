##############################################################################
#    Computer Project #6
#
#    Algortithm
#    Prompt for 6 different options
#    Based off choice different functions will be called
#    Overall this program reads a file and extracts specific data
#    This program can extract median income values from counties in a state
#    With the median_income values it can calculate the states average
#    It can also identify the top 10 counties, and states by income
#    as well as the bottom 10
#
##############################################################################
import csv
from operator import itemgetter
#This list acts as a reference of all the states for easy comparison
STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#Start of functions

def open_file(ch):
    '''This function opens a file for reading'''
    while True: 
        if ch == "r":
            x = input('Input a file: ')
            try:
                fp = open(x, 'r')
    
                return fp
            except  FileNotFoundError:
                print("Invalid filename, please try again.")


def get_county_state(s):
    """This function returns a string separated by commas"""
    s = s.split(',')
    county = s[0].strip()
    state = s[1].strip()
    return county, state
         
def read_file(fp):
    """This function extracts the state, county, and median income \
        and returns a list of sorted tuples"""
    master_list = []
    reader = csv.reader(fp) # set up the reader
    header = next(reader,None) # skip a header
    for line_lst in reader: # loop through the file
        median_income = line_lst[10].replace(',', '')
        if median_income != '' and median_income != None:
            area = line_lst[1]
            county, state = get_county_state(area)
            x = (state, county, int(median_income))
            master_list.append(x)
    master_list = sorted(master_list, key = itemgetter(2), reverse = True)
    return master_list

def state_average_income(state, master_list):
    """This function takes the median income from each county in a \
        state and returns the average income"""
    income_tot = []
    for i in master_list:
        median_income = i[2]
        if i[0] == state:
            income_tot.append(median_income)
    
    if income_tot == []:
        return None
    else:
        average_income = sum(income_tot) / len(income_tot)
        return round(average_income, 2)   
#For both counties by income functions, master list is already 
#sorted in the correct pattern, so it just needed to be indexed 
def top_counties_by_income(master_list):
    """This function returns the top ten counties with the highest income"""
    top_counties = master_list[:10]
    return(top_counties)

def bottom_counties_by_income(master_list):
    """This function returns the bottom ten counties with the lowest income"""
    bottom_counties = master_list[-10:]
    return(bottom_counties)

def top_states_by_income(master_list):
    """This function returns the top ten states by average median \
        incomes in decreasing order"""
    states_income = []
    for element in STATES:
        y = state_average_income(element, master_list)
        if y == None:
            continue
        states_income.append( (element, y))
    states_income.sort(key = itemgetter(1), reverse = True)
    
    return states_income[:10]
        
def bottom_states_by_income(master_list):
    """This function returns the bottom ten states by average median \
        incomes in decreasing order"""
    states_income = []
    for element in STATES:
        y = state_average_income(element, master_list)
        if y == None:
            continue
        states_income.append( (element, y))
    states_income.sort(key = itemgetter(1), reverse = False)
    
    return states_income[:10]
    
def counties_in_state(state, master_list):
    """This function returns a list of tuples with the counties and \
        their median incomes in the state sorted in ascending order"""
    counties_in_state = []
    for element in master_list:
        county = element[1]
        median_income = element[2]
        county_tuple = (county, median_income)
        if state == element[0]:
            counties_in_state.append(county_tuple)
    counties_in_state = sorted(counties_in_state, key = itemgetter(0))
    return counties_in_state
# This function just displays a menu of different options
# for the user to choose from        
def display_options():
    """
    DO NOT CHANGE
    Display menu of options for program
    """
    OPTIONS = """\nMenu
    1: Average median household income in a state
    2: Highest median household income counties
    3: Lowest median household income counties
    4: Highest average median household income states
    5: Lowest average median household income states
    6: List counties' median household income in a state\n"""
    print(OPTIONS)
#This function allows the user to choose between 6 options and they 
#each involve a different function from above
def main():
    print("\nMedian Income Data")
    option_input = ''
    call_open = open_file('r')
    master = read_file(call_open)
    
    
    while option_input != 'q':
        display_options()
        option_input = input('Choose an option, q to quit: ')

#Start of if statements for the 6 options        
        
        if option_input == '1':
            state_code = input('Please enter a 2-letter state code: ')
            while not state_code in STATES:
                print('Please input a valid state')
                state_code = input('Please enter a 2-letter state code: ')
            if state_code in STATES:
                call_av = state_average_income(state_code, master)
                print('\nAverage median income in {:2s}:\
                      ${:<10,.2f}'.format(state_code, call_av))

            
        if option_input == '2':
            top_county = top_counties_by_income(master)
            print('\nTop 10 Counties by Median Household Income (2018)')
            print('{:<10}{:<30s}{:10s}'.format('State', \
                                    'County', 'Median Household Income'))
            for element in top_county:
                print('{:<10}{:<30s}${:<10,d}'.format(element[0], \
                                                      element[1], element[2]))
            
        if option_input == '3':
            bottom_county = bottom_counties_by_income(master)
            print('\nBottom 10 Counties by Median Household Income (2018)')
            print('{:<10}{:<30s}{:<10s}'.format('State', 'County', \
                                                'Median Household Income'))
            for element in bottom_county:
                print('{:<10}{:<30s}${:<10,d}'.format(element[0], \
                                                      element[1], element[2]))

            
        if option_input == '4':
            top_state = top_states_by_income(master)
            print('\nTop 10 States by Average Median Household Income (2018)')
            print('{:<10}{:<10s}'.format('State', 'Median Household Income'))
            for element in top_state:
               print('{:<10}${:<10,.2f}'.format(element[0], element[1])) 
            
        if option_input == '5':
            bottom_state = bottom_states_by_income(master)
            print('\nBottom 10 States by Average Median \
                  Household Income (2018)')
            print('{:<10}{:<10s}'.format('State', 'Median Household Income'))
            for element in bottom_state:
                print('{:<10}${:<10,.2f}'.format(element[0], element[1]))
            
            
        if option_input == '6':
            
            state_code = input('Please enter a 2-letter state code: ')
            if state_code in STATES:
                state_counties = counties_in_state(state_code, master)
                num_counties = len(state_counties)
                if num_counties < 1:
                    print('\nThere are 0 counties in {}'.format(state_code))
                else:
                    print('\nThere are {} counties in {}:'.format\
                          (num_counties, state_code))
                    print('{:<30s}{:<10}'.format('County', 'Median \
                                                 Household Income'))
                for element in state_counties:
                    print('{:<30s}${:<10,d}'.format(element[0], element[1]))
            else:
                print('Please input a valid state')
                state_code = input('Please enter a 2-letter state code: ')
        if option_input > '6' and option_input != 'q':
            print('Invalid choice, please try again')
            
if __name__ == '__main__':
    main()