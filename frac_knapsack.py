
"""
Created on Sun Nov  3 18:29:28 2019

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
    highest ratio to decreasing ratio to acknowledge priority. What the algorithm will do is enter whole number 
    weights of the objects into the bag then fill in the remaining portion through a fractional amount. 
'''
#will read in my data to organize the rows by columns 
import pandas as pd 

def frac_knapsack(file, max_weight):
    #will read in my data as a dataframe
    df = pd.read_csv(file)
    
    #held into another variable so we can add another column to sort from 
    holder = df
    
    #this will add a separate column known as ratio to sort by 
    holder['RATIO'] = holder['VALUE'] / holder['WEIGHT']
    
    #will sort by ascending the column along with the rest of data according to ratio
    holder.sort_values('RATIO', inplace = True, ascending = True)
    
    #holds the data after the sort which is the object, weights, and values
    packables = list(holder.iloc[0:,0])    
    values = list(holder.iloc[0:,1])
    weights = list(holder.iloc[0:,2])
    #to count th weights that are being added 
    weight_sum = 0
    #what is being held and what the index iterations will involve 
    value_objects = []
    #this makes sense that element iteration will be the length of what is in the csv file 
    i = len(packables)
    #what is being appended to the bag based on checking through the ratio sort of the data
    knapsack_container = []
    
    
    #while the max weight is greater than 0 and the iteration is greater than 0 go through the loop
    while max_weight > 0 and i > 0:
        #this is decrementing because we are going backwards in iteration because the data structure is 
        #structured in ascending order 
        i -= 1
        #if weight element is less than the max weight of the knapsack, then the threshold will decrement
        #by that weight
        if weights[i] < max_weight:
            #then I can add the weight that was added to the sum of of weight that is added so far
            weight_sum += weights[i]
            #while that decrements by that weight
            max_weight -= weights[i]           
            #then I can also add the value of that object too
            value_objects.append(values[i])
            #then I can also add the object element that was added into the knapsack
            knapsack_container.append(packables[i])
            
            #the above statement takes care of whole numbers, so while it decremented, gettign closer
            #to the max weight of the knapsack, it will enter by fractional details 
        else:
            #the max weight dividied by the weight of the element will be held int this var
            frac_item = max_weight/weights[i]
            #this looks at fraction multipled by the value of that element to append into the items list
            value_objects.append(values[i] * frac_item)
            #this will decrement the weight by the fraction multipled by the weight element from the remainder 
            max_weight -= (weights[i] * frac_item)
            #this will continue to add to the sum weight by fractional input 
            weight_sum += (weights[i] * frac_item)
            
    return 'The list of objects is: '+str(knapsack_container), ' The sum weight of the objects are: '+str(weight_sum),' The sum values of the items is: '+ str(sum(value_objects)) 

            
            
            
#    print("Item values:", value_objects, 'sum of the item values', sum(value_objects))
#    print("Total Weight value:", weight_sum)
#    print("The knapsack contains:", knapsack_container)


print(frac_knapsack('Assignment9.csv', 1000))




