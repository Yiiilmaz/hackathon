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

def hasCycle(m, index):
    visited = [0] * index
    for v in range(index):
        for u in range(index):
            visited[u] = -1
        if (dfsCycleCheck(m, index, v, v, visited)):
            return True
    return False


def dfsCycleCheck(m, index, v, u, visited):
    visited[v] = False
    for w in range(index):
        if ( m[v][w] == 0): # Most likely wrong
                if not visited[w]:
                    if dfsCycleCheck(index, v, u, visited):
                        return True
                elif (w != u):
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
            edge_list.append({'i' : i, 'j' : j, 'w' : G[i][j]})
    edge_list.sort(key=get_weight)
    for edge in edge_list:
        MST = add_edge(MST, edge)
        num_edges += 1
        #if theres a cycle drop the edge
        if hasCycle(MST, size):
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
    


        
     


        



