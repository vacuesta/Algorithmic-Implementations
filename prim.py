
"""
Created on Mon Nov 11 19:09:52 2019

@author: vincentacuesta
"""
import pandas as pd
#import networkx as nx
#import matplotlib.pyplot as plt
from heapq import heappop, heappush

def prim(file):
    #pandas read csv tab delimited
    df = pd.read_csv(file, delimiter = '\t')
#    print(df)
    #column values
    from_here = list(df.iloc[0:,0])
    to = list(df.iloc[0:,1])
    dist = list(df.iloc[0:,3])
#    print(dist)
    #store graph in dictionary 
    locations = {}
    #counter for elements
    i = 0
    #keep track of unique nodes in a set 
    uniqueNode = set()
#    print(uniqueNode) 
    
    
#origin = list(df.iloc[0:,0])
#dest = list(df.iloc[0:,1])
#dist = list(df.iloc[0:,3])
#data = list(zip(dest,dist))
#
#final_data = list(zip(origin,data))
#
#G = nx.Graph()
#G.add__weighted_edges_from(final_data)  
    
    #Note to user: having trouble organizing data as a graph with networkx module
    #decided to try using a for loop to organize the dictinary. For some reason
    #network x puts too many dictionaries within dictionaries which makes it
    #difficult for iteration 
    for node1 in from_here:
        uniqueNode.add(node1)
        if node1 in locations:
            locations[node1][to[i]] = dist[i]
        else:
            locations[node1] = dict([(to[i],dist[i])])
            
        if to[i] in locations:
            locations[to[i]][node1] = dist[i]
        else:
            locations[to[i]] = dict([(node1,dist[i])])
        
        i += 1
    #graph is held in locations
    G = locations
    
    #implementation to prims algorithm with heap. Tuple edges and start node 
    #track has to do with the queue
    tuples,track = [],[(0,None,'HOUSTON')]
    
    #length of railing with a set of the nodes 
    railing = 0
    nodes = set()
    
    #keeping track of that queue
    while track: 
        #looking at the length and the end and start node keep track, heappop
        length, end, start = heappop(track)
        
        #if the start node is in the set keep going 
        if start in nodes: 
            continue        
        #if the end node is not None
        #add the start nodes to the set 
        if end != None:
            nodes.add(start)
            #the tuples should then append the start and end node 
            tuples.append((start, end))
            #for each appendage add the railing 
            railing += length
        #if the start node is in the graph then for the neighbor in the start items  
        for neighbor, dist in G[start].items():
            #heappush within the tracked elelements and the start connected to 
            #the neighbor
            heappush(track, (dist, start, neighbor))   
    
    return 'The tuple edges are :'+ str(tuples),'The total length of road laid out :' +str(railing)

print(prim('Texas.txt'))

    
    
    
