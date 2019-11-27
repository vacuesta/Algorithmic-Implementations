"""
Created on Fri Nov 15 18:48:18 2019

@author: vincentacuesta
"""
'''
pseudocode: functools decorator to store subproblem calculations that can be returned by using the @functools.lru_cache(). 
Inputs into the function are 2 different strings. It's a type of recursive implementation so I will put in the base cases and then the call the function. Do the minimum of the calculations that involve the insertion, deletion and substition portions. Which then returns the edit distance.
'''

import functools
#from functools import wraps

#memo decorator that stores values of evaluated subproblems from the recursion for easy return 
@functools.lru_cache()
def editDist_memo(str1, str2):

    #check input of string 1 to return the length of the available string
    if not str1: return len(str2)
    #Check input of string 2 to return the length of the available string 
    elif not str2: return len(str1)
    #compare the character of the string from the end 
    elif str1[-1] != str2[-1]:
        #if it is the same then there is no expense to change it 
        expense = 1
    else:
        #if it is not the same then add 1 because there is a change that needs to be done 
        expense = 0
        
    #return the value of the minimum changes needed for the insertion, deletion and substitution for the substrings   
    return min([editDist_memo(str1[:-1], str2)+1,
               editDist_memo(str1, str2[:-1])+1, 
               editDist_memo(str1[:-1], str2[:-1]) + expense])
    
print(editDist_memo('djfasdkfjasldkfja', "laskdjfalsdkfjalsdkfjalksdfjalskdfjalksdjfalksdjfalksdjfalskdjfalksdjfalskdfjalskdfjalksdfjalksdjfalsdkjfalksdjfalskdjflaskdjflasdkjfalsdkjfalskdjfalskdjflaskdjflaksdjfalsdkjfalsdkjfalsdkjfalsd"))