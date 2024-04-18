def islandPerimeter(self, grid: List[List[int]]) -> int:
    cnt_ones = 0
    cnt_near = 0
    dircs = {(0,1),(1,0),(0,-1),(-1,0)}
    for i, l in enumerate(grid):
        for j, v in enumerate(l):
            if v == 1:
            cnt_ones += 1
        else:
                continue
            for ai,aj in dircs:
                ni,nj = ai+i,aj+j
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]==1:
                    cnt_near += 1
    return 4*cnt_ones - cnt_near
