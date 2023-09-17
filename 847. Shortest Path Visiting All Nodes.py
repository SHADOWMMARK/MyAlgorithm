'''
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. 
You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node.
You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

'''
from collections import deque
def shortestPathLength(graph) -> int:
    # basic idea is using the BFS to solve but add a mask to record the route and deque = [(mask,node)..] to keep record
    n = len(graph)
    que = deque([(1<<i,i) for i in range(n)])
    # and we need to record how far we have gone at this node using this mask (route)
    dic = {(1<<i,i):0 for i in range(n)}

    while que:
        mask,node = que.popleft()
        d = dic[(mask,node)]

        if mask == (1 << n) - 1: #if every node has been visited
            print((1 << n) - 1,1 << n - 1)
            return d

        for neighbor in graph[node]:
            new_mask = mask | 1<<neighbor
            if (new_mask,neighbor) not in dic.keys():
                dic[(new_mask,neighbor)] = d+1
                que.append((new_mask,neighbor))

print(shortestPathLength(graph=[[1,2,3],[0],[0],[0]]))