#read unconnected towns
#read internet nodes
#construct relationship matrix
#populate relationship matrix
#do a minimal spanning tree
#produce a list of connections

import numpy as np
import csv


def find_distance(town1, town2):
    return np.sqrt((town1.x - town2.x) ** 2 + (town1.y - town2.y) ** 2)


towns = []
index = 0
with open('towns.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        towns.append({
        'name' : 
        'x' :
        'y' :
        'index' : index,
        'node_type' : 'town'
        })
        index++

with open('nodes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        towns.append({
        'name' : 
        'x' :
        'y' :
        'index' : index,
        'node_type' : 'node'
        })
        index++

m = np.zeros(index,index)
for town1 in towns:

    if town1['node_type'] == 'town':
        for town2 in towns if town2['node_type'] == 'town': 
            m[town1.index][town2.index] = find_distance(town1, town2)
            m[town2.index][town1.index] = find_distance(town1, town2)
            
    if town1['node_type'] == 'node':
        for town2 in towns if town2['node_type'] == 'node': 
            m[town1.index][town2.index] = 0
            m[town2.index][town1.index] = 0
            
def cycle_check():
    pass

KruskalMST(G):
  MST=empty graph
  sort edges(G) by weight
  for each e ∈ sortedEdgeList:
    MST = MST ∪ {e}  // add edge
    if MST has a cyle:
      MST = MST \ {e}  // drop edge 
    if MST has n-1 edges:
      return MST


        



