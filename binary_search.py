
"""
Created on Mon Sep 23 20:05:27 2019

@author: vincentacuesta
"""

def binary_search(thisList, goal):
    #take advantage of the list that is sorted
    #divide and conquer the problem
    #split the list in half and look at the middle element
    #is the element greater than? which means it is in the upper half in the aray and vice versa
    
    #index of last element
    lastelm = len(thisList) - 1
    
    #index of first element
    firstelm = 0
    
    i = -1
    
    #search algorithm
    #determine middle element of the array 
    while (i == -1) and (firstelm <= lastelm):
        #low and high over 2 is mid element
        mid = (firstelm + lastelm) // 2
        
        #is the goal equal to mid element of list? then yes we found it
        if goal == thisList[mid]:
            i = mid
            return str(i) + ' is the position of this goal in the list'
        #if the goal is less than mid point then we can just look at the lower part of array and set middle as high
        elif goal < thisList[mid]:
            lastelm = mid - 1
        else:
            #this will just do the vice versa of what is mentioned above
            firstelm = mid + 1
    return 'This is not in list'
    
    



#to check the list if it contains the goal number
thisList = list(range(1000))
goal = 90

print(binary_search(thisList, goal))