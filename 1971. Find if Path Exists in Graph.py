'''
build a dictionary recording source -> destination routes
BFS the routes to find if it is possible to reach, if not return False
'''
def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination: return True
    di = defaultdict(list)
    for a,b in edges:
        di[a].append(b)
        di[b].append(a)
    visited = {source}
    temp = di[source]
    while temp:
        ntemp = []
        for v in temp:
            if v == destination:
                return True
            if v in visited:
                continue
            else:
                visited.add(v)
                ntemp.extend(di[v])
        temp = ntemp
    return False
