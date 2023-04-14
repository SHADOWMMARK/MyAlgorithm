from typing import List
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    ans = []
    m,n = len(matrix),len(matrix[0])
    top,bot,left,right = 0, m-1, 0, n-1

    while top <= bot and left <= right:
        for j in range(left,right+1):
            ans.append(matrix[top][j])
        top += 1
        for i in range(top,bot+1):
            ans.append(matrix[i][right])
        right -= 1

        if top <= bot:
            for j in range(right,left-1,-1):
                ans.append(matrix[bot][j])
            bot -= 1

        if left<=right:
            for i in range(bot,top-1,-1):
                ans.append(matrix[i][left])
            left += 1
    return ans