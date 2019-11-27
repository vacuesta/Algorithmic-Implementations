
"""
Created on Sat Oct 26 18:00:36 2019

@author: vincentacuesta
"""
'''
pseudocode:
    Try marking key points for each of the buildings
    going from left to right from top to bottom.
    if another section overlaps but the height is bigger
    than you change the y coordinate. Remove redundant points
    that are not necessary for describing the sky line.
    Looking at each subsection. Do something where you look at the left coordinate
    of the building and elevate all those lower until you see the right side of building
    So based on adding one building at a time this would end up in going in quadratic. But 
    if i was able to think of this by just comparing the x values into a separate list and then 
    modifying based on height max and replacing it if it got elevated than I can see this being done
    in linear time. Organize the input to take out the height and iterate through the x values and make logic
    to set height to 0 to then elevate based on iteration through building heights for skyline
'''
buildings = [(3, 13, 9), (1, 11, 5), (12, 7, 16), (14, 3, 25), (19, 18, 22), (2, 6, 7), (23, 13, 29), (23, 4, 28)]

def make_skyline_one_by_one(buildings):
    
    pos_recent = None #this will be in regards to the height, right now it is set to none but will change based on max height
    skyline = [] #we will append to this making the list of skyline points 
    x_coord = [] #we will be taking the x coordinates out of the input list for comparison
    x_coord.extend([building[0],building[2]] for building in buildings) #in each triple, the x coordinates will be taken out
    x_coord = sorted([item for sublist in x_coord for item in sublist]) #makes flat list of x values and sorts them in order
    #I tried doing the one line above but this means it takes out my data in O(n^2)
    
    
    #for element in list we are now checking the comparisons between x coordinates
    for i in x_coord:
        check_x = [] #now comes the logic comparison for iteration through the x coordinates
        #extend into the x list if the building[0] is less than the iteration of i element and building[2] is greater
        #this logic will help find the x coordinate in the x coord list where the x coord is less than the other
        check_x.extend(building for building in buildings if (building[0] <= i and building[2] > i))
        
        #for the logic done in checking in those x values. If that value is not in the list then the position height will
        #start at 0 and you will append whatever that element was with that height 0
        if not check_x:
            pos_recent = 0
            skyline.append((i,0))
            continue
        #with the logic created above, we are going to look to maximize top height
        #if that is the max in the iteration through check_x then you will replace that max height
        top_height = max(building[1] for building in check_x)
        
        #the final logic to check if that top_height is not equal to the pos_recent then you replace the pos_recent
        if top_height != pos_recent:
            #the final logic to keep appending the x coord with that max height
            pos_recent = top_height
            
            #append each time that i element in the list with the max height but this accounts 
            #for getting rid of the redundancies because of the if then logic and list
            skyline.append((i,top_height))
            #sL = [item for sublist in skyline for item in sublist]
            
    return skyline#return value skyline with x and max height coordinates
    

tuple_skyline = make_skyline_one_by_one(buildings)
newskyline = [item for sublist in tuple_skyline for item in sublist]
print(newskyline)


