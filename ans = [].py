board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "SEE"
dircs={(-1,0),(1,0),(0,1),(0,-1)}
l = len(word)
m=len(board)
n=len(board[0])

def dfs(k,q):
    tempi,tempj = q
    if k==l :
        print(q)
        print(1)
        return True
    for i,j in dircs:
        ni, nj = tempi+ i , tempj+j
        if ni>=0 and ni<m and nj>=0 and nj<n and k<l and board[ni][nj]==word[k]:    
            dfs(k+1,(ni,nj))
for i in range(m):
    for j in range(n):
        if word[0] == board[i][j]:
            q=(i,j)
            dfs(1,q)
    


