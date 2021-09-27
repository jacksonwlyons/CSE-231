##############################################################################
#    Computer Project #11
#
#    Algortithm
#    Matrix class
#    Calculate different matrices
#    Build methods to complete different calculations/conversions 
#    Error check to verify if calculation is valid
#    Variations of multiple methods can be calculated
#    
##############################################################################

'''Matrix Class'''


class Matrix(object):
    def __init__(self, num_rows=2, num_cols=2):
        '''
         This function intitializes a matrix
        '''
        if num_rows < 0  and num_cols < 0:
            raise ValueError("Matrix: Error, the dimensions must be positive integers!")
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.array = [[0 for x in range(num_cols)] for y in range(num_rows)]
        
    def __str__(self):
        '''
         This function returns a string representation of the matrix
        '''
        x = '['
        for row in self.array:
            x+='['
            for i in row:
                x+= str(i)    #build format for matrix
                x+= ' '
            x = x.strip()
            x+=']\n '
        x = x.strip()    
        x+=']'
        return(x.strip())
            
    def __repr__(self):
        '''
        Returns the same string as __str__
        '''
        Matrix.__str__()
    
    def __getitem__(self, iijj):
        '''
         This function allows us to get the values from the matrix
        '''
        
        
        if type(iijj) == int:   #index can be a single integer or a tuple of two values
            if not iijj > 0:
                raise IndexError ("Matrix: Error, bad indexing!")
            elif iijj > self.num_rows:
                raise IndexError ("Matrix: Error, index out of range!")
            return self.array[iijj -1]
        if type(iijj) == tuple:
            
            row = iijj[0]
            col = iijj[1]
           
            if type(row) != int or type(col) != int:
                raise ValueError ('Matrix: Error, the indices must be a positive integer or a tuple of integers!')
  
            if iijj[0] <= 0 or iijj[1] <= 0:
                raise IndexError ("Matrix: Error, bad indexing!")
            if row > len(self.array) or col > len(self.array[0]):
                raise IndexError ("Matrix: Error, index out of range!")
     
            else:
                return self.array[row-1][col-1]

        else:
            raise ValueError ("Matrix: Error, the indices must be a positive integer or a tuple of integers!")

    
    def __setitem__(self, iijj, value):
        '''
        This function allows us to set the values from the matrix,
        similar to __getitem__
        '''
        if type(value) != float and type(value) != int:
            raise ValueError ('Matrix: Error, You can only assign a float or int to a matrix!')

        if type(iijj) != tuple:
            raise ValueError ('Matrix: Error, the indices must be a tuple of integers!')
        
        if type(iijj) == tuple:
            
            if type(iijj[0]) != int or type(iijj[1]) != int:
                raise ValueError ('Matrix: Error, the indices must be a tuple of integers!')
            if iijj[0] <= 0 or iijj[1] <= 0:
                raise IndexError ("Matrix: Error, bad indexing!")
            
            row = iijj[0]
            col = iijj[1]
          
            if row > len(self.array) or col > len(self.array[0]):
                raise IndexError ("Matrix: Error, index out of range!")
     
            else:
                self.array[row-1][col-1] = value  #set specific index equal to value
                return self.array[row-1][col-1]

        
    
    def __add__(self,B):
        '''
        This function performs a matrix addition
        '''
        if type(B) == int:
            raise ValueError ('Matrix: Error, you can only add a matrix to another matrix!')
        if len(self.array) != len(B.array):
            raise ValueError ('Matrix: Error, matrices dimensions must agree in addition!')
        
        new_matrix = Matrix(len(self.array), len(self.array[0]))
        for j in range(len(self.array)):
            for k in range(len(self.array[j])):
                x = self.array[j][k] + B.array[j][k] #add values from each matrix at the same index
                
                new_matrix[j+1, k+1] = x
        return new_matrix
    
    
    def dot_product(self,L1,L2):
        '''
         This function returns the dot product of two lists of numbers
        '''
        
        if len(L1) != len(L2):
            raise ValueError ("Dot Product: must be same length")
        sum1 = 0
        for i in range(len(L2)): #iterate through each num in lists
            x = L1[i] * L2[i]   #multiply corresponding numbers
            sum1 += x
        return sum1
                                     
        
    def __mul__(self,B):
        '''
        This function performs the multiplication of two matrices
        '''
        
        if not isinstance(B, Matrix):
            raise ValueError ('Matrix: Error, you can only multiply a matrix to another matrix!')
        if self.num_cols != B.num_rows:
            raise ValueError ('Matrix: Error, matrices dimensions must agree in multiplication!')

        new_matrix = Matrix(len(self.array), len(B.array[0]))

        for col in range(B.num_cols):
            Bcol_vals = []  #B matrix column values
            for rows in range(B.num_rows):
                Bcol_vals.append(B[rows+1, col+1])
   
            for i in range(self.num_rows):
                
                temp_list = self[i+1]
                dot = self.dot_product(temp_list, Bcol_vals)  #calculate dot product for each col for each row
                new_matrix[i+1, col+1] = dot
            
        return new_matrix

    def transpose(self):
        '''
        This function returns the transpose of the matrix. 
        *swap rows and columns*
        '''
        new_matrix = Matrix(len(self.array[0]), len(self.array))
       
        for k in range(len(self.array)): # iterate through rows
            for j in range(len(self.array[0])):   #iterate through columns
                new_matrix[j+1, k+1] = self[k+1, j+1]  #swap rows and columns

        return new_matrix
        
    def __eq__(self,B):
        '''
        This function returns True if corresponding values are equal, 
        and False otherwise
        '''
        for row1 in self.array:
            for row2 in B.array:   #iterate through rows and cols check if matrices are equal
                if row1 == row2:
                    return True
        else:
            return False
    
    def __rmul__(self,i):
        '''
         This function performs a scalar multiplication 
         (int * matrix)
        '''
        if type(i) != int:
            raise ValueError ("Matrix Error: scaler must be an int.")
        
        row1 = len(self.array)
        col1 = len(self.array[0])
        new_mat = Matrix(row1, col1)  #create new matrix
        
        for row_number in range(len(self.array)):
            for col_number in range(len(self.array[0])):
                new_mat[row_number+1, col_number+1] = self[row_number+1, col_number+1] * i  # +1 to account for difference indexing matrix vs python indexing
            
        return new_mat
        
#end class