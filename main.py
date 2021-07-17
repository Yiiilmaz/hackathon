#read unconnected towns
#read internet nodes
#construct relationship matrix
#populate relationship matrix
#do a minimal spanning tree
#produce a list of connections

import numpy as np
import matplotlib.pyplot as plt
import csv


def find_distance(town1, town2):
    return np.sqrt((town1['x'] - town2['x']) ** 2 + (town1['y'] - town2['y']) ** 2)

def get_weight(edge):
    return edge['w']

def adjacent(G, v, w, size):
    return (w != v and G[w][v] != -1)


def isCyclicUtil(graph, v, u, visited, size):
    visited[v] = True
    for w in range(size):
        if (adjacent(graph, v, w, size)):
            if not visited[w]:
                if isCyclicUtil(graph, w, v, visited, size):
                    return True
            elif w != u:
                return True;
    

    return False

def isCyclic(graph, size):
   
    result = False
    visited = [False] * size
    for v in range(size):
        for i in range(size):
            visited[i] = False
        if isCyclicUtil(graph, v, v, visited, size):
            result = True
            break;
    return result
    


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
            if G[i][j] != -1 and i != j:
                edge_list.append({'i' : i, 'j' : j, 'w' : G[i][j]})
    
    edge_list.sort(key=get_weight)
    print(edge_list)
    for edge in edge_list:
        
        
        MST = add_edge(MST, edge)
        print(MST)
        print(isCyclic(MST, size))
        num_edges += 1
        #if theres a cycle drop the edge
        if isCyclic(MST, size):
            num_edges -= 1
            
            edge['w'] = -1
            MST = add_edge(MST, edge)
        if num_edges == size - 1:
            return MST
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
        'x' : float(row[1]),
        'y' : float(row[2]),
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
        'x' : float(row[1]),
        'y' : float(row[2]),
        'index' : index,
        'node_type' : 'node'
        })
        index += 1


m = np.zeros((index,index))
m[:] = -1
for town1 in towns:
    if town1['node_type'] == 'town':
        for town2 in towns:
                
            m[town1['index']][town2['index']] = find_distance(town1, town2)
            m[town2['index']][town1['index']] = find_distance(town1, town2)
            
    if town1['node_type'] == 'node':
        for town2 in towns:
            if town2['node_type'] == 'node': 
                m[town1['index']][town2['index']] = 0
                m[town2['index']][town1['index']] = 0
    
#print(m)
MST = KruskalMST(m, index)
print(MST)

xs = []
ys = []
for i in range(index):
    for j in range(i, index):
        if adjacent(MST, i, j, index) and MST[i][j] != 0:
            
            plt.plot([towns[i]['x'], towns[j]['x']], [towns[i]['y'], towns[j]['y']], 'y')


plt.plot(   [town['x'] for town in towns if town['node_type'] == 'town'], [town['y'] for town in towns if town['node_type'] == 'town'], 'ro',
            [town['x'] for town in towns if town['node_type'] == 'node'], [town['y'] for town in towns if town['node_type'] == 'node'], 'bs' ,
     )
plt.show()


        
     


        



