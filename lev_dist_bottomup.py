
"""
Created on Fri Nov 15 18:48:18 2019

@author: vincentacuesta
"""
'''pseudocode:
    inputs are 2 different strings and this goes by a bottom-up relaxed implementation of dynamic programming . This is a matrix type implementation where conceptually the bottom right digit from the matrix is the cost of the edit distance from all the tangled dependencies. I have to add an index to the strings in the iteration to skip a 0 in the beginning. It works like filling up a table.
'''
import numpy as np 

def editDist_bottomUp(str1, str2):
    
    #formation of the matrix, adding one to skip one value of the index which is the 0 at the upper left hand corner this is to ensure each element has its own cell for easy counting 
    top_x = len(str1)+1
    side_y = len(str2)+1
    #numpy to make the matrix 
    matrix = np.zeros((len(str1)+1, len (str2)+1))
#    print(matrix)
    #counters
    val = 0
    val1 = 0 
    
    #prints out t through the range of integers down the rows 
    while val < len(matrix[0,:]):
        matrix[0,val] = val
        val += 1
#    print(matrix)
    
    #prints out range of integers down columns 
    while val1 < len(matrix[:,0]):
        matrix[val1,0] = val1
        val1 += 1
#    print(matrix)


    
    #the logic goes by in the comparison for the updating of the matrix to get the edit distance    
    for col in range(1, side_y):
        #then goes throw the rows with the numbers made from the matrix
        for row in range(1, top_x):
            #with the comparison of characters through the matrix, if the last character is equal then there is no expense and if it is equal then there will be an expense change of 1
            if str1[row-1] == str2[col-1]:
                expense = 0
            else:
                expense = 1
                #logic from the elements of matrix[row][col] comparisons in the matrix for the insertion, deletion and subsition
            matrix[row][col] = min(matrix[row-1][col] + 1,     
                                 matrix[row][col-1] + 1,     
                                 matrix[row-1][col-1] + expense) 
#    print(matrix)
    
 
    return int(matrix[row][col])

print(editDist_bottomUp("", ""))
