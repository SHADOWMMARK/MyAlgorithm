grid = [[0,1],[1,0]]
def shortestBridge(grid) -> int:
    ans= 0
    n = len(grid)
    visited = [[0]*n for _ in range(n)]
    
    near = {(-1,0),(1,0),(0,-1),(0,1)}
    allq = []
    k = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and k ==0:
                que = [(i,j)]
                visited[i][j] = 1
                allq.append((i,j))
                while que:
                    oi,oj = que.pop(0)
                    for ai,aj in near:
                        ni,nj = ai+oi,aj+oj
                        if 0<=ni<n and 0<=nj<n and visited[ni][nj] != 1 and grid[ni][nj]==1:
                            que.append((ni,nj))
                            visited[ni][nj] = 1
                            allq.append((ni,nj))
                k = 1

    que = allq
    while que:
        nextq = []
        while que:
            oi,oj = que.pop(0)
            for ai,aj in near:
                ni,nj = ai+oi,aj+oj
                if 0<=ni<n and 0<=nj<n and visited[ni][nj] != 1 and (ni,nj) not in nextq and grid[ni][nj]==1:
                    return ans
                elif 0<=ni<n and 0<=nj<n and visited[ni][nj] != 1:
                    nextq.append((ni,nj))
        que = nextq
        ans += 1
    return -1
print(shortestBridge(grid))