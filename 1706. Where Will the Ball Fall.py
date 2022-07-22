#using the BFS like algorithm, layer by layer solve the problem
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        ans = [0]*n
        
        if grid[0][0] == -1:
            ans[0] = -1
        elif n>1:
            if grid[0][1]==-1:
                ans[0] = -1
            else:
                ans[0] = 1
                    
        if grid[0][-1] == 1:
            ans[-1] = -1
        elif n>1:
            if grid[0][-2]==1:
                ans[-1] = -1
            else:
                ans[-1] = n-2
        for i in range(1,n-1):
            if grid[0][i] == 1:
                if grid[0][i+1] == -1:
                    ans[i] = -1
                else:
                    ans[i] = i + 1
            else:
                if grid[0][i-1] == 1:
                    ans[i] = -1
                else:
                    ans[i] = i-1
        for j in range(1,m):
            for i in range(n):
                temp = ans[i]
                
                if temp == -1:
                    continue
                    
                if temp == 0: 
                    if grid[j][0] == -1:
                        ans[i] = -1
                    else:
                        ans[i] = 1
                    continue
                    
                if temp==n-1:
                    if grid[j][-1] == 1:
                        ans[i] = -1
                    else:
                        ans[i] = n-2
                    continue
                    
                if grid[j][temp] == 1:
                    if grid[j][temp+1] == -1:
                        ans[i] = -1
                    else:
                        ans[i] += 1
                else:
                    if grid[j][temp-1] == 1:
                        ans[i] = -1
                    else:
                        ans[i] -= 1
        return ans
        
