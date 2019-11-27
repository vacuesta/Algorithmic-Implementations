
"""
Created on Sun Nov  3 18:29:39 2019

@author: vincentacuesta
"""
'''
pseudocode:
    the parameters entered will follow the file name that will be in the working directory along with the maximum
    weight for the bag. The idea of this function is to optimize the objects that have the best worth into the 
    bag without looking back. Data is organized by using pandas to read in the rows of columns. iloc is the 
    function that is used to do. After organizing data with lists to hold item values, objects into the bag,
    and the sum of the weight, the logic may take place. In addition, after adding another column of ratio that 
    divides the value and weight, then we can optimize which objects belong in the bag, but this will sort from
    highest ratio to decreasing ratio to acknowledge priority. The algorithmic process of this function will
    add objects by a 0 and 1 method aka it will only add whole objects as it decrements down the list of objects
    that is based on the ratio. If the next object doesn't fix, then it will stop adding to the knapsack.
'''


import pandas as pd

#file = "Assignment9.csv"

def knapsack(file, max_weight):
    #will read in my data as a dataframe
    df = pd.read_csv(file)
    
    #held into another variable so we can add another column to sort from 
    holder = df
    
    #this will add a separate column known as ratio to sort by 
    holder['RATIO'] = holder['VALUE'] / holder['WEIGHT']
    
    #will sort by ascending the column along with the rest of data according to ratio
    holder.sort_values('RATIO', inplace = True, ascending = True)
    
    #will hold the data by rows of the specific columns 
    packables = list(holder.iloc[0:,0])
    weights = list(holder.iloc[0:,2])
    values = list(holder.iloc[0:,1])
    #print(packables)
    #the incremental counter of teh weights that are being added to the container in regards to max weight 
    weight_sum = 0
    #will hold the values of the objects that are being appended to this list 
    value_objects = []
    #element iteration that will be the length of the whole list of objects
    i = len(packables)
    #the knapsack container that will have objects appended to it that are added 
    knapsack_container = []
    
    
    #while the max weight is greater than 0 and the elemental iteration is greater than 0 
    while max_weight > 0 and i > 0:
        #the decremental iteration because the data structure is organizing the values by ascending 
        i -= 1
        #if the elemental weight is less than the max weight of the container
        if weights[i] < max_weight:
            #it will append the whole number value for that object into this list
            value_objects.append(values[i])
            #the max weight that is left will decrement by the weight of the object that is added here 
            max_weight -= weights[i]
            #the weights of the objects that are being appended will sum up and be returned
            weight_sum += weights[i]
            #for everything that is added, it will be appended into the container as whole objects 
            knapsack_container.append(packables[i])
            
    return 'The list of objects is: '+str(knapsack_container), ' The sum weight of the objects are: '+str(weight_sum),' The sum values of the items is: '+ str(sum(value_objects)) 
            
#    print('The items in the bag are:',knapsack_container)
#    print('The sum weight of the objects in the bag are:', weight_sum)
#    print('The sum values of the objects in the bag are:', sum(value_objects))
#        
print(knapsack('Assignment9.csv', 1000))
#knapsack('Assignment9.csv', 1000)


