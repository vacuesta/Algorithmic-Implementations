
"""
Created on Mon Nov  4 20:46:40 2019

@author: vincentacuesta
"""
'''
pseudocode:
    my input will involve the same file and max weight. This wil be similar to the integer knapsack problem 
    that i wrote but instead of stopping there, the problem is going to lookback and change what it can to 
    maximize the value output of the objects in the back. The way I thought about this is just modifiying the
    code that I wrote then having some type of holder/temporary value that will be changed and popped within 
    another while loop, and it will continue to back propagate until it finds a better object to put in.
'''
import pandas as pd

def check_again_knapsack(file, max_weight):
    #make the dataframe of the data       
    df = pd.read_csv(file)
    #holder for the data in order to add a column 
    df_frame = df
    #to add the new column that will help organize how to look at the data
    df_frame['RATIO'] = df_frame['VALUE'] / df_frame['WEIGHT']
    #add the ratio column based on the value divided by height in ascending order 
    df_frame.sort_values('RATIO', inplace = True, ascending = True)
    #uses iloc method in order to read row by row in a columnar fashion 
    packables = list(df_frame.iloc[0:,0])
    weights = list(df_frame.iloc[0:,2])
    values = list(df_frame.iloc[0:,1])
    #list for the values of the items 
    val_item = []
    #iteration through however making it to the length of the list in the csv 
    i = len(packables)
    #list to keep track of what is being put into the container
    container = []
    #counter for the sum weight of what is beign put into the bag 
    weight_sum = 0
    
    #while the max weight is greater than 0 and the iteration is greater than 0 
    while max_weight > 0 and i > 0 :
        #will decrement as it checks down the list 
        i -= 1
        #a separate iteration by j just because we don't go back on the same i iteration 
        j = i-1
        #if that elemental weight is less than the max weight 
        if weights[i] < max_weight:
            #It will append to the values list becasue this part is similar to the interger knapsack 
            val_item.append(values[i])
            #will reduce from the max weight
            max_weight -= weights[i]
            #will add the weights that are added to the sum weight counter
            weight_sum += weights[i]
            #time to hold the templ value to keep track of that object
            temp_val = values[i]
            #also holds the temporary weight of that object
            temp = weights[i]
            #then append to the container with that object
            container.append(packables[i])
        #if that max weight with the weight of the last objct subtracting taht weight is geater than 0
        #this is so we do't go over the max weight of the suitcase
        elif(temp + max_weight - weights[i]) >=0:   
            #if j is greater than 0 with the value of one and teh the index of the other less than temp value
            while j>0 and (weights[i] + weights[j]) <= temp_val:
                j -= 1
                
            #If the element value at i and j is greater than the temp value 
            #i use values here to make sure i'm optimizing the object added as i go back to check
            if (values[i] + values[j]) > temp_val:
                #pop the last object in the container 
                container.pop()
                #add teh temp weight to the threshold to give back that weight 
                max_weight += temp
                #subtract that temp weight from the sum to keep track of that last item popped
                weight_sum -= temp
                #add items to the list from the next iteration 
                container.append(packables[j])
                #add items to the list from that iteration 
                container.append(packables[i])
                #the max weight subtracting the weight of the element that is added until it goes to max possible fill
                max_weight -= weights[i]
                #adding the weight to the sum weight counter 
                weight_sum += weights[i]
         
            return 'The container has: '+str(container),'The sum weight of the container is: '+str(weight_sum)
                
                            
print(check_again_knapsack('Assignment9.csv', 1000) )                  
            
