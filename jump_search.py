
"""
Created on Mon Sep 23 20:06:32 2019

@author: vincentacuesta
"""

'''
Algorithm for sorted arrays to check fewer elements compared to a linear search
This array of size n will be jumped at a size m
I will have to do a jump then a linear search til the end of the list
The jump will be sqrt() of the length of the list
'''
import math

def jump_search( n , goal , thisList ): 
    
    #This the amount of jumps that will take place from 
    #index 0 when taking the square root of the array length
    jumps = math.sqrt(n) 
      
    #this will loop under the condition to see which block the goal is in
    #if the minimum number of jumps taken is less than the goal, then that previous pointer is equal to the jumps
    point = 0
    while thisList[int(min(jumps, n)-1)] < goal: 
        point = jumps
        jumps += math.sqrt(n) 
        if point >= n: 
            return 'nada'
      
    #this loop will check if the point is less than the goal, if it is, then it will linear search
    #increment towards where the goal is. 
    while thisList[int(point)] < goal: 
        point += 1
          
        # this checks if the element was not present at all, at which it will return a negation
        if point == min(jumps, n): 
            return 'nada'
      
    # If element is found in the list then it will return this 
    if thisList[int(point)] == goal: 
        return 'This in list'
      
    return 'This not in list'

thisList = list(range(1000))
goal = 70
n = len(thisList)

print(jump_search(n, goal, thisList))



