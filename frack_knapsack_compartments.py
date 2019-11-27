
"""
Created on Sun Nov  3 18:29:56 2019

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
    highest ratio to decreasing ratio to acknowledge priority. The way this will work is by spliting the knapsack 
    half and this means that the max weight of the whole container will be split in half and the algorithm will
    add to both left and right compartments. The fractional method will keep adding bits of the last object until
    it fills the max weight of both compartments. 
'''
#will help organize the data into data frames 
import pandas as pd

def frac_knapsack(file, max_weight):
    #will read the data in as a dataframe 
    df = pd.read_csv(file)
    
    #this will be used as a holder that will be used to add another column that is based on 
    holder = df
    #will add the ratio volumn into the data frame 
    holder['RATIO'] = holder['VALUE'] / holder['WEIGHT']
    #will sort the ratio with corresponding objects and values into an ascending order 
    holder.sort_values('RATIO', inplace = True, ascending = True)
    #the purpose of iloc here is from pandas so that you can read all rows of a specific column 
    packables = list(df.iloc[0:,0])
    weights = list(df.iloc[0:,2])
    values = list(df.iloc[0:,1])
    
    #this will be an elemental iteration from the length of the list of objects 
    i = len(packables)
    #this portion is needed to iterate through the other compartment but so it doesn't overlap with i iteration
    j = i - 1
    #the weights sum of the left compartment
    sum_wl= 0
    #the weight sum of the right compartment
    sum_wr=0
    #the left compartment to keep track of for objects
    left_compartment = []
    #the right compartment to keep trac of for the objects
    right_compartment = []
    #the values for the left 
    values_left = []
    #the values for the right compartment
    values_right = []
    #the max weight divided by 2 for the left side
    hf_left = max_weight/2
    #the max weight divided by 2 for the right side 
    hf_right = max_weight/2
    #the loop will make sure that it will iterate for both left and right compartments
    while (hf_left > 0 and i > 0)or( j >0 and hf_right > 0):
        #the decremental iteration because it goes by less every other. Technically the objects added
        #should be the same if their was no separator.
        i -= 2
        j -= 2
        #the logic here are 2 separate conditionals to add to the left or right compartments
        #it adds in a way so it does not add duplicates of items into the compartment
        #this works the same way as if i was removing an object from the orignal list to be added to the other
        if packables[i] not in right_compartment:
            #if the elemental weight is less than half of the max weight of the compartment 
            if weights[i] < hf_left:
                #will decrement the weight value from that half max value for the left compartment 
                hf_left -= weights[i]
                #this will add the object weights of what are being added into the sum of weights counter
                sum_wl += weights[i]
                #this will append objects to the list 
                left_compartment.append(packables[i])
                #this will appen values into the left compartment of those objects 
                values_left.append(values[i])
            else:
                #the fractional logic comes in where the fraction of the item is held in this var
                frac_item = hf_left/weights[i]
                #append item values based on this after there is merely a fraction left
                values_left.append(values[i] * frac_item)
                #continue to decrement the max weight based on the fraction remaining 
                hf_left -= (weights[i] * frac_item)
                #continue to add to that max weight counter to fill in the remainder
                sum_wl+= (weights[i] * frac_item)
        #this is the same logic as above to not affect dupicates. So we can add into the right bag with no dupes        
        if packables[j] not in left_compartment:
            #if the weight of this separate iteration is less than the max weight of the other side
            if weights[j] <hf_right:
                #decrement the elemental weight not in the max weight of the other side 
                hf_right -= weights[j]
                #add the elemental weight into the sum
                sum_wr += weights[j]
                #add the objects into the right bag
                right_compartment.append(packables[j])
                #the item values into the right designated list for values of objects 
                values_right.append(values[j])
            else:
                #hold the fract value
                frac_item = hf_right/weights[j]
                #append the item values that is acting as the remainder for the space 
                values_right.append(values[j] * frac_item)
                #decrement from the remaining max weight 
                hf_right -= (weights[j] * frac_item)
                #add to the remaining weight
                sum_wr+= (weights[j] * frac_item)
                
    return 'Left compartment has: '+str(left_compartment),'\n Sum of left compartment: '+str(sum_wl),' Sum of values left: '+str(sum(values_left)),'Right compartment has: '+str(right_compartment),' Sum of right compartment: '+str(sum_wr),' Sum of values right: '+str(sum(values_right))

            
    
#    print('items left:', items_left, 'sum of values', sum(items_left))       
#    print('left bag is:' ,left_bag)
#    print('The sum of left compartment', sum_wl)
#    
#    print('items right:', items_right, 'sum of values', sum(items_right))
#    print('right bag is:' , right_bag)
#    print('The sum of right compartment', sum_wr)


print(frac_knapsack('Assignment9.csv', 1000))
#frac_knapsack('Assignment9.csv', 1000)





