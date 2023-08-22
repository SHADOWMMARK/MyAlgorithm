class Solution:
    """
    here I used two sets to record, but if no extra space needed, we could use  2 bit,
    let the second bit to be the changed one
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        arounds = {(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)}
        m,n = len(board),len(board[0])
        nextL = set()
        nextD = set()
        def checkAround(i,j):
            lives,dies = 0,0
            for ai,aj in arounds:
                ni,nj = i+ai,j+aj
                if 0<=ni<m and 0<=nj<n:
                    if board[ni][nj]==1:
                        lives+=1
                    else:
                        dies+=1
            if board[i][j] == 1:
                if lives<=1:
                    nextD.add((i,j))
                elif lives>3 and lives!=2 and lives!=3:
                    nextD.add((i,j))
            elif board[i][j] == 0 and lives == 3:
                nextL.add((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                checkAround(i,j)
        for i,j in nextL:
            board[i][j] = 1
        for i,j in nextD:
            board[i][j] = 0
        