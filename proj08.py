##############################################################################
#    Computer Project #8
#
#    Algortithm
#    Open 3 files for reading (income, GDP, population)
#    Prompt for a specific region or all regions
#    Calculate min/max of GDP and income per capita
#    Display states wth those min/max values
#    Display data for all states in region
#    Prompt for plot
#    If user wants a plot they are then prompted to choose x and y values
#
##############################################################################

import csv, pylab
from operator import itemgetter

REGION_LIST = ['Far West',
 'Great Lakes',
 'Mideast',
 'New England',
 'Plains',
 'Rocky Mountain',
 'Southeast',
 'Southwest',
 'all']
STATES = ['Alabama',
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'District of Columbia',
 'Florida',
 'Georgia',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Kentucky',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'Rhode Island',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming']

PROMPT1 = "\nSpecify a region from this list or 'q' to quit -- \nFar West,Great Lakes,Mideast,New England,Plains,Rocky Mountain,Southeast,Southwest,all: "

def open_file(s):
    '''This function opens 3 files for reading'''
    while True: 
        if s == 'income':
            x = input('Input a income file: ')
            try:
                fp = open(x, 'r')
    
                return fp
            except  FileNotFoundError:
                print("Invalid filename, please try again.")
        elif s == 'GDP':
            x = input('Input a GDP file: ')
            try:
                fp = open(x, 'r')
    
                return fp
            except  FileNotFoundError:
                print("Invalid filename, please try again.")
        elif s == 'population':
            x = input('Input a population file: ')
            try:
                fp = open(x, 'r')
    
                return fp
            except  FileNotFoundError:
                print("Invalid filename, please try again.")
            
def read_income_file(fp):
    '''This function reads a income file and builds a dictionary with the \
        region and income for each state'''
    region = ''
    D = {}
    reader = csv.reader(fp) # set up the reader
    header = next(reader,None) # skip 5 lines
    header = next(reader,None)
    header = next(reader,None)
    header = next(reader,None)
    header = next(reader,None)
    for line in reader: # loop through the file
        val_list = []
        if line[0].strip() in STATES:
            state = line[0]
            state = state.strip()
            income = line[6].replace(',', '')
            income = int(income)
            val_list.append(region)
            val_list.append(income)
            D[state] = val_list
        else:
            region = line[0].strip()
             
    return D

def read_gdp_file(fp,D):
    '''This function reads a GDP file and adds more data to the \ 
        dictionary (D). The data will contain region, \ 
            income, and GDP for each state'''
    region = ''
    reader = csv.reader(fp) # set up the reader
    header = next(reader,None) # skip 6 lines
    header = next(reader,None)
    header = next(reader,None)
    header = next(reader,None)
    header = next(reader,None)
    header = next(reader,None)
    for line in reader: # loop through the file
        if line[0].strip() in STATES:
            state = line[0]
            state = state.strip()
            gdp = line[7].replace(',', '')
            gdp = int(gdp)
            D[state].append(gdp)
        else:
            region = line[0].strip()
    return D

def read_pop_file(fp,D):
    '''This function reads a population file and adds more data to the \ 
        dictionary (D). The data will contain region, \ 
            income, GDP, and population per million for each state'''
    reader = csv.reader(fp) # set up the reader
    header = next(reader,None) # skip 1 line
    for line in reader: # loop through the file
        if line[1].strip() in STATES:
            state = line[1]
            state = state.strip()
            pop = line[2].replace(',', '')
            pop = int(pop)
            pop = round((pop / 1000000), 2)
            D[state].append(pop)

    return D

def get_min_max(D,region):
    '''This function will extract data for a specified region and determine \ 
        the min/max for both income and GDP'''
    cap_data = []
    if region in REGION_LIST:
        for state,val_list in D.items():
            if val_list[0] == region or region == 'all':
                income_percap = int(val_list[1])
                income_percap = round(income_percap / val_list[3])
                GDP_percap = int(val_list[2])
                GDP_percap = round(GDP_percap / val_list[3])
                x = (state, income_percap, GDP_percap)
                cap_data.append(x)
        
        income_data = sorted(cap_data, key=itemgetter(1))
        gdp_data = sorted(cap_data, key=itemgetter(2))
        income_max = income_data[0]
        income_min = income_data[-1]
        gdp_max = gdp_data[0]
        gdp_min = gdp_data[-1]
        return income_max, income_min, gdp_max, gdp_min
    if region not in REGION_LIST:
        return None
    
            
def get_region_states(D,region):
    '''This function builds a list of tuples of data for states in the \
        specified region'''
    region_data = []
    if region in REGION_LIST:
        for state, val_list in D.items():
            if state == 'District of Columbia':
                state = 'DC'
            if val_list[0] == region or region == 'all':
                population = val_list[3]
                income = int(val_list[1])
                income_percap = round(income / val_list[3])
                GDP = int(val_list[2])
                GDP_percap = round(GDP / val_list[3])
                x = (state, population, GDP, income, GDP_percap, income_percap)
                region_data.append(x)
        
        state_data = sorted(region_data, key=itemgetter(0))
        return state_data
                
        
    if region not in REGION_LIST:
        return None
        
    
def display_region(D,region):
    '''This function will display data for a different \
        regions or all regions. It will display min & max income and \
            GDP; regions’ state data'''
    if region not in REGION_LIST:
        return None
    elif region == 'all':
        print("\nData for the all regions:")
    elif region != 'all':
        print("\nData for the {:s} region:".format(region))
        
    income_max, income_min, gdp_max, gdp_min = get_min_max(D, region)
    print("\n{:s} has the highest GDP per capita at ${:,d} ".format(gdp_min[0], gdp_min[2]))
    print("{:s} has the lowest GDP per capita at ${:,d} ".format(gdp_max[0], gdp_max[2]))
    print("\n{:s} has the highest Income per capita at ${:,d} ".format(income_min[0], income_min[1]))
    print("{:s} has the lowest Income per capita at ${:,d} ".format(income_max[0], income_max[1]))
    region_s = get_region_states(D, region)
    print("\nData for all states in the {:s} region:".format(region))
    print("\n{:15s}{:>13s}{:>10s}{:>12s}{:>18s}{:>20s}".format('State','Population(m)','GDP(m)','Income(m)','GDP per capita','Income per capita'))
    for info in sorted(region_s):
        print("{:15s}{:>13,.2f}{:10,d}{:12,d}{:18,d}{:20,d}".format(info[0], info[1], info[2], info[3], info[4], info[5]))
        
        
def plot_regression(x,y):
    '''
        This function plots the regression line between 2 variables. 
        This function is provided in the skeleton code.
        
        Parameters:            
            x: a list that includes the values for the first variable
            y: a list that includes the values for the second variable
                                
        Returns: None
    '''
    #set the size of the plot
    pylab.rcParams['figure.figsize'] = 6.4, 4.8
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    #fit a line, only takes numpy arrays
    m,b = pylab.polyfit(xarr,yarr, deg = 1) 
    #plotting the regression line
    pylab.plot(xarr,m*xarr + b, '-') 

def plot(region_states):
    '''
        This function plots the data (GDP, population, Income, GDP per capita, and
        Income per capita) for the selected region. It also plots the regression
        line between 2 of the data. This function is provided in the skeleton code.
        
        Parameters:            
            region_states (list of tuples): list of tuples of data for states 
            in the specified regio (state, population, GDP,income, 
                                    GDP per capita, and income per capita)
                                
        Returns: None
    '''
    
    VALUES_LIST = ['Pop', 'GDP', 'PI', 'GDPp', 'PIp']
    VALUES_NAMES = ['Population(m)','GDP(m)','Income(m)','GDP per capita','Income per capita']
    PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, GDPp, PIp: "
    
    # prompt for which values to plot
    while True:
        x_name, y_name = input(PROMPT2).strip().split()
        if x_name.lower() in [s.lower() for s in VALUES_LIST] \
           and y_name.lower() in [s.lower() for s in VALUES_LIST]:
               break
        else:
            print("Error in selection. Please try again.")
            
    x_index = VALUES_LIST.index(x_name)
    y_index = VALUES_LIST.index(y_name)
    #print("indices:",x_name,":",x_index," ; ", y_name, ":",y_index)

    # +1 accounts for skipping state name in list
    x = [state[x_index+1] for state in region_states]
    y = [state[y_index+1] for state in region_states]
    state_names = [state[0] for state in region_states]
    
    # get full names
    x_name = VALUES_NAMES[x_index]
    y_name = VALUES_NAMES[y_index]

    # Set the labels and titles of the plot
    pylab.title(x_name + " vs. " + y_name)   #title

    pylab.xlabel(x_name)   #label x axis
    pylab.ylabel(y_name)   #label y axis
    
    #plot the scatter plot   
    pylab.scatter(x,y)
    for i, txt in enumerate(state_names): 
        pylab.annotate(txt, (x[i],y[i]))
    
    #plot the regression line between x and y
    plot_regression(x,y)
    
    #save and show the graph
    pylab.savefig("plot.png",dpi = 100)  
    pylab.show()      
    



def main():
    fp = open_file('income')
    D = read_income_file(fp)
    fp = open_file('GDP')
    D = read_gdp_file(fp, D)
    fp = open_file('population')
    D = read_pop_file(fp, D)
    region_in = input(PROMPT1)
    while not (region_in in REGION_LIST or region_in.lower() == 'q'):
            region_in = input(PROMPT1)
    while region_in.lower() != 'q':
        display_region(D,region_in)
        plot_r = input("\nDo you want to create a plot? ")
        if plot_r.lower() == 'yes':
            x = get_region_states(D, region_in)
            plot(x)
        region_in = input(PROMPT1)
        while not (region_in in REGION_LIST or region_in.lower() == 'q'):
            region_in = input(PROMPT1)
        

if __name__ == '__main__':
    main()       