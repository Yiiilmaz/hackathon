'''hasCycle(G):
|  Input  graph G
|  Output true if G has a cycle, false otherwise
|
|  choose any vertex v ∈ G
|  return dfsCycleCheck(G,v)

dfsCycleCheck(G,v):
|  mark v as visited
|  for each (v,w) ∈ edges(G) do
|  |  if w has been visited then  // found cycle
|  |     return true
|  |  else if dfsCycleCheck(G,w) then
|  |     return true
|  end for
|  return false  // no cycle at v

'''

def hasCycle(index):
    visited = [-1] * index
    for v in range(index):
        visited = [-1] * index
        if (dfsCycleCheck(index, v, visited)):
            return True

    return False

def dfsCycleCheck(index, v, visited):
    visited[v] = True
    for w in range(index):
        if (m[v][w]):
            if visited[w]:
                return True
            elif (dfsCycleCheck(index, w)):
                return True
    return False