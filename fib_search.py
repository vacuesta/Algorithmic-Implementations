
"""
Created on Mon Sep 23 20:16:26 2019

@author: vincentacuesta
"""

'''
logic: the fib number that is to be substracted decreases as the list decreases

'''


def fibonacci_search(thisList, goal): 
    
    
    if len(thisList) == 0:
        return 'This list is empty' 
    
    offthis = -1;
     
    #this is basically the fibonacci generator without using a function
    #the first part measn that it is fib -2 which is equal to 0 the first number
    fib_minus_2 = 0
    #this means the 2nd fib number which is fib(1) which is equal to 1
    fib_minus_1 = 1
    #this is the formula to gain other fib numbers based on the index
    fib = fib_minus_1 + fib_minus_2

    #while the fib number is less the length of the list'
    #a switch is happening here where the values of the variables are switched which is then given to the fib
    #this while statement calculates the fib with the length of the array 
    while (fib < len(thisList)):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2
        
        #this index is utilized to eliminate portions of the list where we did not find the number in the list
    
    #while this fib is greater than 1 
    #the index is chosen by the minimum of the index + the fib-2 and the length of the list
    #this i portion is to ensure that the code doesn't break
    while (fib > 1):
        #this min portion is put in so the code doesn't break
        i = min(offthis + fib_minus_2, (len(thisList)-1))
       #this basically contains the cases of 2 and 3
        #if the goal is less than this index in the list where if you didn't get the value then everything that is above
        #can be eliminated if the goal is less than
        #this is where the list gets smaller
        if (goal > thisList[i]):
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            #then onces the calcluations of the fibs keep happening after all the elminations we will return the index when it is true
            #narrowing down with fib numbers to find the value           
            offthis = i
            
            #continued logic of the calculation to shorten the list if that index in the list is greater than the goal
        else:
            if (goal < thisList[i]):
                fib = fib_minus_2
                fib_minus_1 = fib_minus_1 - fib_minus_2
                fib_minus_2 = fib - fib_minus_1
            else:
                return str(i) + ' is the index of the number that is in the list'
        
        #this condition utilizes the fib numbers to see if it has already passed all values in the list
        #this would mean that if '1 and the index is less than the higest value and value above is the same as the goal
        #then return the value
        #if not you can return that this value is not in the list
        #this also helps to check the first case 1
        #this will run if there is one element left 
    if(fib_minus_1 and offthis < (len(thisList)-1) and thisList[offthis + 1] == goal):
        return offthis + 1;
    return 'This is not in the list'

thisList = list(range(1000))
goal = -1

print(fibonacci_search(thisList, goal))






