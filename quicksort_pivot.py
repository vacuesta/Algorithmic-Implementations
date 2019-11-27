
"""
Created on Sat Oct 26 18:00:35 2019

@author: vincentacuesta
"""

'''
pseudocode:
    Reading in sections of buildings from a list. compare key
    points reading from left to right. In the comparison, the
    value with a lesser x value will be chosen. For that x value
    that is chosen, if that y value is less than last seen 
    height, update key point y to last seen height of other skyline.
    Continue along next key point. Continue until sections are completed.
    Remove redundancy. However the main difference comes in because we have to do a D&C
    If the length of buildings is 1 then return buildings, if not then split the bulidingds into 2
    sections. Solve the left and right recursively then combine the skyline points. I will compare syntax
    of merge sort to this problem to reduce it to my knowledge but implement the logic of the skyline
    to find the points of it. More into thought. What if I organize the data into what I need. Solve skyline recursively both ends 
    until i hit the base case of a vew values left, then linearly combine all data? Which means I may be able
    to incorporlate logic from the 1A into this 
'''

buildings = [(3, 13, 9), (1, 11, 5), (12, 7, 16), (14, 3, 25), (19, 18, 22), (2, 6, 7), (23, 13, 29), (23, 4, 28)]

def mergeSort(alist):    

   #print("Splitting ",alist)
   pos_recent = None
   skyline = []
   x_coord = []
   x_coord.extend([building[0], building[2]] for building in buildings)
   x_coord = sorted([item for sublist in x_coord for item in sublist])
   
   if len(alist)>1:
       mid = len(x_coord)//2
       lefthalf = x_coord[:mid]
       righthalf = x_coord[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

  # print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
    
    
    

    
    
    
    
    
    
    
    
    
    
	
