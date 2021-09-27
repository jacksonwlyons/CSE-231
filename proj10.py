##############################################################################
#    Computer Project #10
#
#    Algortithm
#    Seahaven Solitaire game
#    Class
#    Prompt for choice input/menu
#    Build methods to validate and choose between different options 
#    Display current game
#    Game is won once foundation is full
#    User can quit to end the game
#
##############################################################################

# Solitaire: Seahaven

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from end of Tableau column s to end of column d.
    MTC s d: Move card from end of Tableau column s to Cells d.
    MCT s d: Move card from Cells s to end of Tableau column d.
    MTF s d: Move card from end of Tableau column s to Foundation d.
    MCF s d: Move card from end of Cell s to Foundation d.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''

def initialize():
    '''
        Create and initialize the tableau, foundation and cells,
        and then returns them as a tuple
    '''
    stock = cards.Deck()
    stock.shuffle()
    tableau = [[], [], [], [], [], [], [], [], [], []] 
    foundation = [[],[],[],[]]
    cells = [None, None, None, None] # 4 empty spots in cells, two cards added to middle

    for i in range(5):
        for j in range(10):   #10 columns in tableau for 5 each
            tableau[j].append(stock.deal())
    for k in range(1,3):    # fill two middle spots in cells
        cells[k] = stock.deal()
    init_tup = (tableau, foundation, cells)
    return init_tup
    
    #return tableau, foundation, cells

def display(tableau, foundation, cells):
    '''Display the cell and foundation at the top.
       Display the tableau below.'''
       
    print("\n{:<11s}{:^16s}{:>10s}".format( "foundation","cell", "foundation"))
    print("{:>14s}{:>4s}{:>4s}{:>4s}".format( "1","2","3","4"))
    for i,f in enumerate(foundation):
        if f and (i == 0 or i == 1):
            print(f[-1],end=' ')  # print first card in stack(list) on foundation
        elif i == 0 or i == 1:
            print("{:4s}".format( " "),end='') # fill space where card would be so foundation gets printed in the right place
    print("{:3s}".format(' '),end='')
    for c in cells:
        if c:
            print(c,end=' ')  # print first card in stack(list) on foundation
        else:
            print("[  ]",end='') # fill space where card would be so foundation gets printed in the right place
    print("{:3s}".format(' '),end='')
    for i,f in enumerate(foundation):
        if f and (i == 2 or i == 3):
            print(f[-1],end=' ')  # print first card in stack(list) on foundation
        elif i == 2 or i == 3:
            print("{}{}".format( " ", " "),end='') # fill space where card would be so foundation gets printed in the right place
        
    print()
    print("\ntableau")
    print("   ",end=' ')
    for i in range(1,11):
        print("{:>2d} ".format(i),end=' ')
    print()
    # determine the number of rows in the longest column        
    max_col = max([len(i) for i in tableau])
    for row in range(max_col):
        print("{:>2d}".format(row+1),end=' ')
        for col in range(10):
            # check that a card exists before trying to print it
            if row < len(tableau[col]):
                print(tableau[col][row],end=' ')
            else:
                print("   ",end=' ')
        print()  # carriage return at the end of each row
    print()  # carriage return after printing the whole tableau
    
        
def validate_move_within_tableau(tableau,src_col,dst_col):
    '''
        This function checks to see if move within tableau is legal
    '''
    try:
        mov_card = tableau[src_col][-1] #fixes index out of range error
    except:
        return False
    if mov_card == None:
        return False
    if len(tableau[dst_col]) == 0:
        if mov_card.rank() == 13: #Only king can be added to empty column in tableau
            return True
        else:
            return False
    dst_card = tableau[dst_col][-1]
    if mov_card.suit() != dst_card.suit() or mov_card.rank() != (dst_card.rank()-1):
        return False
    else:
        return True
    
def validate_move_cell_to_tableau(tableau,cells,cell_no,dst_col):
    '''
        This function checks to see if the move from cell to tableau is legal
    '''
    cel_card = cells[cell_no]
    if cells[cell_no] == None:
        return False
    if len(tableau[dst_col]) == 0:
        if cel_card.rank() == 13: #Only king can be added to empty column in tableau
            return True
        else:
            return False
    try:
        dst_card = tableau[dst_col][-1]  #index out of range fix
    except:
        return False
    if cel_card.suit() != dst_card.suit() or cel_card.rank() != (dst_card.rank()-1):
        return False
    else:
        return True
    
def validate_move_tableau_to_cell(tableau,cells,src_col,cell_no):
    '''
       This function checks to see if the move from tableau to cell is legal
    '''
    if len(tableau[src_col]) == 0:  #check for empty column
        return False
    if cells[cell_no] != None: #check to make sure cell is empty
        return False
    else:
        return True

def validate_move_tableau_to_foundation(tableau,foundation,src_col,found_no):
    '''
        This function checks to see if the move from tableau 
        to foundation is legal
    '''
    try:
        mov_card = tableau[src_col][-1]   #Check for empty tableau/card exists
    except:
        False
    if len(tableau[src_col]) == 0:  #check for empty column
        return False
    if len(foundation[found_no]) == 0:
        if mov_card.rank() == 1: #Only Ace can be added to empty foundation
            return True
        else:
            return False
    try:
        fond_card = foundation[found_no][-1]  # index out of range fix
    except:
        return False
    
    if mov_card.suit() != fond_card.suit() or (fond_card.rank()+1) != mov_card.rank():
        return False
    else:
        return True
    

def validate_move_cell_to_foundation(cells,foundation,cell_no,found_no):
    '''
        This function checks to see if the 
        move from cells to foundation is legal
    '''
    
    try:
        cel_card = cells[cell_no] #this fixes indexing out of range error
    except:
        return False
        
    if cells[cell_no] == None:  #check for empty column
            return False
    
    if len(foundation[found_no]) == 0:
        if cel_card.rank() == 1: #Only Ace can be added to empty foundation
            return True
        else:
            return False
    try:  
        fond_card = foundation[found_no][-1]
    except:
        return False
    if cel_card.suit() != fond_card.suit() or (fond_card.rank()+1) != cel_card.rank():
        return False
    else:
        return True
    
# For the following functions, as long as the corresponding validate function 
# returns true, then the these functions will execute the move

def move_within_tableau(tableau,src_col,dst_col):
    '''
        This function will move the specified card to the specified 
        destination within the tableau
    '''
    x = validate_move_within_tableau(tableau, src_col, dst_col)
    mov_card = tableau[src_col][-1]
    #dst_card = tableau[dst_col][-1]
    if x == True:
        tableau[dst_col].append(mov_card)
        tableau[src_col].pop()
        return True
    else:
        return False

def move_tableau_to_cell(tableau,cells,src_col,cell_no):
    '''
        This function will move the specified card in the tableau to the specified 
        destination in the cells
    '''
    x = validate_move_tableau_to_cell(tableau, cells, src_col, cell_no)
    try:
        mov_card = tableau[src_col][-1]
    except:
        return False
    if x == True:
        cells[cell_no] = mov_card
        tableau[src_col].pop()
        return True
    else:
        return False
        
def move_cell_to_tableau(tableau,cells,cell_no,dst_col):
    '''
        This function will move the specified card in cells to the specified 
        destination within the tableau
    '''
    x = validate_move_cell_to_tableau(tableau, cells, cell_no, dst_col)
    if x == True:
        tableau[dst_col].append(cells[cell_no])
        cells[cell_no] = None
        return True
    else:
        return False

def move_cell_to_foundation(cells,foundation,cell_no,found_no):
    '''
        This function will move the specified card in the cells to the specified 
        destination in the foundation
    '''
    cel_card = cells[cell_no]
    x = validate_move_cell_to_foundation(cells, foundation, cell_no, found_no)
    if x == True:
        foundation[found_no].append(cel_card)
        cells[cell_no] = None
        return True
    else:
        return False
            
def move_tableau_to_foundation(tableau,foundation,src_col,found_no):
    '''
        This function will move the specified card in tableau to the specified 
        destination in the foundation
    '''
    mov_card = tableau[src_col][-1]
    x = validate_move_tableau_to_foundation(tableau, foundation, src_col, found_no)
    if x == True:
        foundation[found_no].append(mov_card)
        tableau[src_col].pop()
        return True
    else:
        return False
                    
def check_for_win(foundation):
    '''
        This function will check to see if the game has been won. 
        If the foundation is full, game is won ie True. Otherwise false.
    '''
    for item in foundation:
        if len(item) != 13:
            return False
        
    return True


def get_option():
    '''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    MTT s d: Move card from end of Tableau column s to end of column d.
    MTC s d: Move card from end of Tableau column s to Cells d.
    MCT s d: Move card from Cells s to end of Tableau column d.
    MTF s d: Move card from end of Tableau column s to Foundation d.
    MCF s d: Move card from Cells s to Foundation d.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
    option = input( "\nInput an option (MTT,MTC,MCT,MTF,MCF,R,H,Q): " )
    option_list = option.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]

    if opt_char == 'M' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0]
        if opt_str in ['MTT','MTC','MCT','MTF','MCF']:
            return [opt_str,int(option_list[1]),int(option_list[2])]
# MXX s d
    print("Error in option:", option)
    return None   # none of the above
 
def main():
    print("\nWelcome to Seahaven Solitaire.\n")
    tableau, foundation, cells = initialize()
    display(tableau, foundation, cells)
    print(MENU)
    # Based off user choice, an action will be executed. ex. move card/play
    while True:
        x = False
        choice = get_option()
        if choice[0] == 'MTT':
            x = move_within_tableau(tableau, (choice[1]-1), (choice[2]-1))
        if choice[0] == 'MTC':
            x = move_tableau_to_cell(tableau, cells, (choice[1]-1), (choice[2]-1))

        if choice[0] == 'MCT':
            x = move_cell_to_tableau(tableau, cells, (choice[1]-1), (choice[2]-1))
  
        if choice[0] == 'MTF':
            x = move_tableau_to_foundation(tableau, foundation, (choice[1]-1), (choice[2]-1))
 
        if choice[0] == 'MCF':
            x = move_cell_to_foundation(cells, foundation, (choice[1]-1), (choice[2]-1))
          
        if choice[0] == 'Q':
            break
        if choice[0] == 'H':
            print(MENU)
        if choice[0] == 'R':
            tableau, foundation, cells = initialize()
            display(tableau, foundation, cells)
            print(MENU)
            
        win = check_for_win(foundation)
        if win == True:
            print("You won!")
            # display the winning game
            display(tableau, foundation, cells)
            print("\n- - - - New Game. - - - -")
            tableau, foundation, cells = initialize()
            # restart the game
            # display the new game
            display(tableau, foundation, cells)
            print(MENU)
            continue
        else:
            if x == True:
                display(tableau, foundation, cells)
            else:
                if len(choice) > 1:
                    print("Error in move: {} , {} , {}".format(choice[0], choice[1], choice[2]))
        
    print("Thank you for playing.")

if __name__ == '__main__':
    main()