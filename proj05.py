##############################################################################
#    Computer Project #5
#
#    Algortithm
#    open a file for writing and reading
#    Process each line and remove commas from data and convert to number
#    Write deaths, population millions, and deathrate to file and console
#
#    If the data is for a G20 country, display it and write it to the file
#    if death rate is worse than US rate, print country name in console
#    Close both files
#
##############################################################################


'''Program comment'''
#G20 are the countries we want to use in our write file. 
G20 = "Argentina, Australia, Brazil, Canada, China, France, Germany, \
    India, Indonesia, Italy, Japan, South Korea, Mexico, Russia, \
    Saudi Arabia, South Africa, Turkey, United Kingdom, USA, European Union"
#US death rate used for easy comparison
US_RATE = 1277.10


def open_file(ch):
    '''This function opens a file for reading or writing'''
    while True: 
#Based off ch, try to open either a writing or reading file        
        if ch == 'w':
            x = input('Enter a file name for writing: ')
            try:
                fp = open(x, 'w')
                return fp
            except IOError:
                print("Error opening file.")
        elif ch == "r":
            x = input('Enter a file name for reading: ')
            try:
                fp = open(x, 'r')
    
                return fp
            except IOError:
                print("Error opening file.")
                
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

def process_line(line):
    ''' This function extracts the country, deaths, and population, 
    and returns the numbers for population and deaths'''
    #Take specific columns of data from the read file and do calculations
    deaths_str = line[25:35].strip()
    country = line[:25].strip()
    population_str = line[-10:].strip()
    pop_flt = handle_commas(population_str, 'float')
    deaths_int = handle_commas(deaths_str, 'int')
    return country, deaths_int, pop_flt


def main():    
    file_obj = open_file("r")
    out = open_file("w")
    #formatting columns for write file
    header1 = 'Country','Deaths','Population','Death Rate'
    header2 = '','','Millions','per Million'
    out.write("{:<20s}{:>10s}{:>14s}{:>14s}\n".format(*header1))
    out.write("{:<20s}{:>10s}{:>14s}{:>14s}\n".format(*header2))
    print("{:<20s}{:>10s}{:>14s}{:>14s}".format(*header1))
    print("{:<20s}{:>10s}{:>14s}{:>14s}".format(*header2))
    country_s = ''
    for line in file_obj:
        country, deaths_int, pop_flt = process_line(line)
        try:
            
            death_rate = round(deaths_int / (pop_flt), 2)
# Determine which data is necessary for write file. We only want g20 data.
            if country in G20:
                out.write("{:<20s}{:>10,d}{:>14,.2f}{:>14,.2f}\n".format\
                          (country, deaths_int, pop_flt, death_rate))
                print("{:<20s}{:>10,d}{:>14,.2f}{:>14,.2f}".format(country, \
                      deaths_int, pop_flt, death_rate))
                if death_rate > US_RATE:
                    country_s += country + ','+ ' '
        except:
            continue

    out.close()
    file_obj.close()
    print("\nCountries with higher death rates than USA per million.")
    print(country_s[:-2])
    

    

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
    
