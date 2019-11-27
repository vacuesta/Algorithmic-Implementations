"""
Created on Fri Nov 15 18:48:18 2019

@author: vincentacuesta
"""

'''
pseudocode: you have 2 options either going the memo or bottom-up route, I will use the memo route using import functools
inputs will be the number of steps that have to be made
2 methods to do this either by memo or bottom-up implementations.
This will consider bottom-up. Relaxed iterating through the matrix where the last cell will be the value. THis is similar to the fib sequence in a way where 1 step can be a value of 1 and 2 steps can either be one whole step or 2 individuals.  


'''
#import functools
#import numpy as np

def hustle(n):
    #if the input step is 1 just return n because there are only those amount of ways to get through 
    if n == 1 : return n
    if n == 2: return 2
    #creation of matrix by setting 1 for all steps in n plus an index
    #it helps with the counter in the matrix if it is 1 for some reason failed at 0 or 2
    matrix = [1 for i in range(n+1)]
#    print(matrix)
    #for elements in the range from 2 going to all steps plus 1 
    for i in range(2, n+1):
        #the element of i in the matrix will be the calculation of going 1 step or 2 steps back
        #this is similar to fib 
        matrix[i] = matrix[i-1] + matrix[i-2]
#        print(matrix)
    #returns the matrix position at the last part in the calculation.
    return matrix[n]
print(hustle(9))


#@functools.lru_cache()




    







