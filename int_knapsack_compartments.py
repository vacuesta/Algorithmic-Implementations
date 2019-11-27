
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
    add to both left and right compartments. The integer method will continue to add whole number objects to
    both left and right compartments until nothing else will be able to fit. 
'''
#will import pandas for reading the data 
import pandas as pd 

#function to read file and max weight 
def knapsack(file, max_weight):
    #make a data frame to read in the csv file 
    df = pd.read_csv(file)
    #holder so that we can add columns and manipulate the data 
    holder = df
    #will add the ratio column
    holder['RATIO'] = holder['VALUE'] / holder['WEIGHT']
    #will sort all data into ascending based on the ratio column
    holder.sort_values('RATIO', inplace = True, ascending = True)
    #uses iloc function to read in row by row of the columns 
    packables = list(holder.iloc[0:,0])
    weights = list(holder.iloc[0:,2])
    values = list(holder.iloc[0:,1])
    items_left = []
    items_right = []
  #  items = []
    #we have to do 2 separate iterations because we have to go through the left and right compartment 
    i = len(packables)
    #this is for the other compartment so we dont do an overlap
    j = i - 1
  #  bag = []
    #the sum of the left compartment 
    sum_wl= 0
    #the sum of the right compartment counter to keep track of 
    sum_wr=0
    #this is the list of the left compartment 
    left_compartment = []
    #this is the list of the right compartment 
    right_compartment = []
    #max weight of the left compartment 
    hf_left = max_weight/2
    #max weight of the right compartment
    hf_right = max_weight/2
    #the while loop to check iterations and for both thresholds that are equal than 0 
    while (hf_left > 0 and i > 0)or( j >0 and hf_right > 0):
        #a counter decrement by -2 to do every other as it checks elements that are more prioritized
        i -= 2
        j -= 2
        #similar logic as the unpartiioned but now we are 
        if packables[i] not in right_compartment:
            #the weight of elemental weights are less than the max weight 
            if weights[i] < hf_left:       
                #append the object values when this condition is met 
                items_left.append(values[i])
                #decrement the elemental weight from the max weight 
                hf_left -= weights[i]
                #add the elemental weight of what is added to the bag to the sum weight of the compartment to keep track 
                sum_wl+= weights[i]
                #then append the objects to the bag 
                left_compartment.append(packables[i])                   
#            new_lv = np.delete(a, index)
#            new_rv = np.delete(a, index)
        #to avoid duplicates you have to make sure whatever is in the right bag is not in the left bag 
        if packables[j] not in left_compartment:
            #condition for elemental weight of the other compartment with half of the max weight 
            if weights[j] < hf_right:
                
                #same logic is happening above where we other adding object value items into this
                items_right.append(values[j])
                #then we are decrementing elemental weights from the max weight
                hf_right-= weights[j]
                #then we are adding that elemental weight to the sum weight counter for that compartment 
                sum_wr+= weights[j]
                #Then append those objects into the bag 
                right_compartment.append(packables[j]) 
                
    return 'Left compartment has: '+str(left_compartment),' Sum of left compartment: '+str(sum_wl),' Sum of values left: '+str(sum(items_left)),'Right compartment has: '+str(right_compartment),' Sum of right compartment: '+str(sum_wr),' Sum of values right: '+str(sum(items_right))
#    return 
       
#    print('items left:', items_left, 'sum of values', sum(items_left))       
#    print('left bag is:' ,left_bag)
#    print('The sum of left compartment', sum_wl)
    
#    print('items right:', items_right, 'sum of values', sum(items_right))
#    print('right bag is:' , right_bag)
#    print('The sum of right compartment', sum_wr)
   
   
print(knapsack('Assignment9.csv', 1000))  
   
   
   
   
   
   
   