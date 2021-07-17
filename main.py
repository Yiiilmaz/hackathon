#read unconnected towns
#read internet nodes
#construct relationship matrix
#populate relationship matrix
#do a minimal spanning tree
#produce a list of connections

import numpy as np
import csv


def find_distance(town1, town2):
    return np.sqrt((town1['x'] - town2['x']) ** 2 + (town1['y'] - town2['y']) ** 2)

def get_weight(edge):
    return edge['w']

def isCyclicUtil(graph, v, visited, parent, size):

    # Mark the current node as visited
    visited[v]= True
    print(graph)
    # Recur for all the vertices
    # adjacent to this vertex
    for i in range(size):
        if (graph[v][i] != -1):
            # If the node is not
            # visited then recurse on it
            if visited[i]==False :
                if(isCyclicUtil(graph,i,visited,v,size)):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif  parent!=i:
                return True
     
    return False

def isCyclic(graph, size):
   
    # Mark all the vertices
    # as not visited
    visited =[False]*(size)
     
    # Call the recursive helper
    # function to detect cycle in different
    # DFS trees
    for i in range(1, size):
        print(visited)
        # Don't recur for u if it
        # is already visited
        if visited[i] == False:
    
            if(isCyclicUtil(graph,i,visited,0,size)) == True:
                return True
     
    return False
    


def add_edge(G, edge):
    G[edge['i']][edge['j']] = edge['w']
    G[edge['j']][edge['i']] = edge['w']
    return G


def KruskalMST(G, size):
    MST = np.zeros((size,size))
    MST[:] = -1
    
    edge_list = []
    num_edges = 0
    for i in range(size):
        for j in range(i, size):
            if G[i][j] != -1:
                edge_list.append({'i' : i, 'j' : j, 'w' : G[i][j]})
    
    edge_list.sort(key=get_weight)
    
    for edge in edge_list:
        MST = add_edge(MST, edge)
        print(isCyclic(MST, size))
        num_edges += 1
        #if theres a cycle drop the edge
        if isCyclic(MST, size):
            num_edges -= 1
            
            edge['w'] = -1
            MST = add_edge(MST, edge)
        if num_edges == size - 1:
            return MST


towns = []
index = 0
with open('towns.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #ignore the header
    next(reader)
    for row in reader:
        towns.append({
        'name' : row[0],
        'x' : int(row[1]),
        'y' : int(row[2]),
        'index' : index,
        'node_type' : 'town'
        })
        index += 1

with open('nodes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #ignore the header
    next(reader)
    for row in reader:
        
        towns.append({
        'name' : row[0],
        'x' : int(row[1]),
        'y' : int(row[2]),
        'index' : index,
        'node_type' : 'node'
        })
        index += 1


m = np.zeros((index,index))
m[:] = -1
for town1 in towns:
    if town1['node_type'] == 'town':
        for town2 in towns:
            if town2['node_type'] == 'town': 
                
                m[town1['index']][town2['index']] = find_distance(town1, town2)
                m[town2['index']][town1['index']] = find_distance(town1, town2)
            
    if town1['node_type'] == 'node':
        for town2 in towns:
            if town2['node_type'] == 'node': 
                m[town1['index']][town2['index']] = 0
                m[town2['index']][town1['index']] = 0
    

MST = KruskalMST(m, index)
print(MST)
    


        
     


        



