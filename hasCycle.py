def hasCycle(index):
    visited = [0] * index
    for v in range(index):
        for u in range(index):
            visited[u] = -1
        if (dfsCycleCheck(index, v, v, visited)):
            return True
    return False


def dfsCycleCheck(index, v, u, visited):
    visited[v] = False
    for w in range(index):
        if ( m[v][w] == 0): # Most likely wrong
                if not visited[w]:
                    if dfsCycleCheck(index, v, u, visited):
                        return True
                elif (w != u):
                    return True
    return False

