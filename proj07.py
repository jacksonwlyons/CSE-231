##############################################################################
#    Computer Project #7
#
#    Algortithm
#    Prompt for a year
#    Based off year input, file is opened for reading
#    Specific data extracted and calculations are done regarding income ranges
#    Average income, median income and other data can be calculated
#    Percentages can be calculated based off income ranges
#    Plot of data is also available
#    If plot is selected, user is prompted with menu of choices 
#    for different calculations/data
#  
##############################################################################
import pylab

def do_plot(x_vals,y_vals,year):
    '''Plot x_vals vs. y_vals where each is a list of numbers \
        of the same length.'''
    pylab.xlabel('')   # Label for X-axis
    pylab.ylabel('')   # Label for Y-axis
    pylab.title("Cumulative Percent for Income in "+\
                str(year))# Title for graph (what is written on top)
    pylab.plot(x_vals,y_vals)    # draws the plot (including labels and title)
    pylab.rcParams['figure.figsize'] = 6.4, 4.8 #  Set the size of the plot
    pylab.savefig("plot.png",dpi = 100)#save plot with specified resolution
    pylab.show()   # displays the plot
    
def open_file():
    '''This function prompts for a year and opens the data file \
        that corresponds with that year. It returns a file pointer and year'''
    data_file = 'yearXXXX.txt'
    year_input = input("Enter a year where 1990 <= year <= 2019: ")
    try:
        int(year_input)
    except:
        print("Error in year. Please try again.")
        year_input = input("Enter a year where 1990 <= year <= 2019: ")
    while int(year_input) < 1990 or int(year_input) > 2019:
        print("Error in year. Please try again.")
        year_input = input("Enter a year where 1990 <= year <= 2019: ")
        if year_input.isdigit and int(year_input) > 1990 and \
            int(year_input) <= 2019:
            break
    data_file = 'year' + year_input + '.txt'
    year_int = int(year_input)
    while True:
        try:
            fp = open(data_file, 'r')
            return fp, year_int
        except:
            print("Error in file name:",data_file," Please try again." )
            year_input = input("Enter a year where 1990 <= year <= 2019: ")
            year_int = int(year_input)
            data_file = 'year' + year_input + '.txt'
            
        
def handle_commas(s,T):
    '''This function removes commas and converts the string to float, \
        int or none'''
    s = s.replace(",", '')
# Based on T, s will be converted to either a string or float.   
    if T == 'int':
        try:
            s = int(s)
            return s
        except: 
            return None
    elif T == 'float':
        try:
            s = float(s)
            return s
        except:
            return None

def read_file(fp):
    '''The function takes in file pointer parameter to read the data file. \
        This function returns a list of tuples'''
    data_lst = []
    fp.readline()
    fp.readline()
    for line in fp:  # loop through the file
        line = line.strip()
        line = line.split()
        if not line[2].isdigit():
            element1 = handle_commas(line[0], 'float')
            element2 = handle_commas(line[2], 'float')
            element3 = handle_commas(line[3], 'int')
            element4 = handle_commas(line[4], 'int')
            element5 = handle_commas(line[5], 'float')
            element6 = handle_commas(line[6], 'float')
            element7 = handle_commas(line[7], 'float')                         
        
            x = ((element1 , element2) , element3, element4, element5, \
                 element6, element7)
            data_lst.append(x)
        else:
            element1 = handle_commas(line[0], 'float')
            element2 = None
            element3 = handle_commas(line[3], 'int')
            element4 = handle_commas(line[4], 'int')
            element5 = handle_commas(line[5], 'float')
            element6 = handle_commas(line[6], 'float')
            element7 = handle_commas(line[7], 'float')                         
        
            x = ((element1 , element2) , element3, element4, element5, \
                 element6, element7)
            data_lst.append(x)
            
    return data_lst  
  
def find_average(data_lst):
    '''Takes a list of data and returns the average salary'''
    income_tot = 0
    number_tot = 0
    for i in data_lst:
        combined_income = i[4]
        income_tot += combined_income
        number = i[1]
        number_tot += number
        
    avg_salary = round(income_tot / number_tot, 2)
    return avg_salary
    
    
def find_median(data_lst):
    '''Takes a list of data and returns the median income'''
    percent1 = 50
    higher = get_range(data_lst, percent1)
    percent2 = 49
    lower = get_range(data_lst, percent2)
    if abs(higher[1] - 50) > abs(lower[1] - 50):
        return(lower[2])
    else:
        return(higher[2])

        
def get_range(data_lst, percent):
    '''Takes a list of data and a percent and returns data for the \
        first data line whose cumulative percentage is greater than \
            or equal to the percent parameter.'''
    for i in data_lst:
        column5 = i[3]
        if column5 >= percent:
            element1 = i[0][0]
            element2 = i[0][1]
            element7 = i[5]
            range_tup = ((element1, element2) , column5, element7)
            return range_tup

def get_percent(data_lst, salary):
    '''Takes a list of data and an income and returns the income range and the
            corresponding cumulative percentage'''
    for i in data_lst:
        
        element1 = i[0][0]
        element2 = i[0][1]
        column5 = i[3]
        if salary >= element1 and salary <= element2:
            percent_tup = ((element1, element2) , column5)
    return percent_tup
            
    
def main():

    fp, year_int = open_file()  
    print("For the year {:4d}:".format(year_int))
    data_lst = read_file(fp)
    avg = find_average(data_lst)
    print("The average income was ${:<13,.2f}".format(avg))
    median1 = find_median(data_lst)
    print("The median income was ${:<13,.2f}".format(median1))
    plot = input("Do you want to plot the data (yes/no): ")
    if plot == 'yes':  
        do_plot(data_lst[0][0], data_lst[3], year_int)
    while True:
         choice = \
      input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")
         if choice == 'r':
             percent_in = input("Enter a percent: ")
             while not percent_in.isdigit() or float(percent_in) > 100 or \
                 float(percent_in) < 0:
                 print("Error in percent. Please try again")
                 percent_in = input("Enter a percent: ")
             percent_in = float(percent_in)
             range_tup = get_range(data_lst, percent_in)
             
             print("{:4.2f}% of incomes are below ${:<13,.2f}.".\
                   format(percent_in, range_tup[0][0]))
         elif choice == 'p':
             income_in = input("Enter an income: ")
             income_in = float(income_in)
             while income_in < 0:
                 print("Error: income must be positive")
                 income_in = input("Enter an income: ")
                 income_in = float(income_in)
             
             percent = get_percent(data_lst, income_in)
             print("An income of ${:<13,.2f} is in the top {:4.2f}% of incomes.".format(income_in, percent[1]))
             
         elif choice == '':
             break
         else:
             print("Error in selection.")
             
if __name__ == '__main__':
    main()