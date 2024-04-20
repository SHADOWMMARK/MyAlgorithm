'''
    Solution toward leetcode problem 1992. Find All Groups of Farmland

    idea is using a visited matrix to keep track what has been visited,
    when meets a land not in the visited and equals 1 and travel toward x,y 
    two directions until meet 0 which means now we get left-top and right-bottom
    corner of the 'group', record it, update the visited matrix then continue
   going through the 'land'.
'''
def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
    m,n = len(land),len(land[0])
    visited = [[0]*n for _ in range(m)]
    dircs = {(0,1),(0,-1),(1,0),(-1,0)}
    ans = []
    for i in range(m):
        for j in range(n):
            if land[i][j]==0:
                continue
            else:
                if visited[i][j] == 1:
                    continue
                ai,aj = 1,1
                while i+ai<m and land[i+ai][j] == 1:
                    ai += 1
                while j+aj<n and land[i][j+aj] == 1:
                    aj += 1
                ans.append([i,j,i+ai-1,j+aj-1])
                for vi in range(i,i+ai):
                    for vj in range(j,j+aj):
                        visited[vi][vj]=1
    return ans


