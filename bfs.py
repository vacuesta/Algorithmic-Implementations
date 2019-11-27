
"""
Created on Mon Oct 21 20:13:56 2019

@author: vincentacuesta
"""

#graph to check distance code 
G = {'A':set(['B','C']),
     'B':set(['D','E','A']),
     'C':set(['A','F','G']),
     'D':set(['B','H','I']),
     'E':set(['B','J','K']),
     'F':set(['C']),
     'G':set(['C','L']),
     'H':set(['D']),
     'I':set(['D','M','N']),
     'J':set(['E']),
     'K':set(['E']),
     'L':set(['G']),
     'M':set(['I']),
     'N':set(['I'])
     }
def bfs(G,initial):
    
    for key in G:
        if len(G[key]) is None: break
    set_seen = set() #you have to maintain a set of the nodes that were visited with no repeats
    count = 0 #incrememnt a count of those visited from intiial
    dist = {initial:None} #this will maintain a dictionary type count to go from the initial to the rest of the nodes
    #a FIFO stack needs to be implemented because that is what a bfs uses

    QUEUE = [(initial, 0)] #keep track of stack to pop off what was already visited and keep going
       
    while QUEUE: #while there are nodes in the queue
        track = QUEUE.pop(0) #need variable to keep track of the pops
   
        component = track[0] #nodes that are being looked at 
        count = track[1]    #perform a count from intitial node to other nodes
        count += 1 #everytime that is appended make a count
        
        for i in G[component]: #iterate to see components in the graph 
            
            if i in set_seen: #if it is in the set then no need to look at the component again 
                continue
            
            set_seen.add(i) #add that element to the set 
            QUEUE.append((i,count)) #add that element along with the count 
           
            dist[i] = count #add that element to the dictionary with the count next to it 
            
    return dist #return dict with nodes from initial and the count distance 


print(bfs(G, 'A'))