class Solution:   
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction =[[-1,0],[1,0],[0,-1],[0,1]]
        self.res=False        
        m = len(board)
        if m ==0: return m==len(word)
        n= len(board[0])
        mark= [[False for j in range(n)] for i in range(m)] 
        
        index =0
        for i in range(m):
            for j in range(n):
                if not mark[i][j] and board[i][j] == word[index]:
                    if self.backtrack(mark,board, word,direction, i,j ,m,n,index):                    
                        return True
        return False    
    
    def backtrack(self,mark,board, word,direction, i,j ,m,n,index):
        if index ==len(word):
            return True
        if not( 0<=i<m and 0<=j<n):
            return False
        if mark[i][j]:
            return False
        if board[i][j] != word[index]:
            return False
        mark[i][j] = True
        ret = False
        for direc in  direction:
            n_i = i + direc[0]
            n_j = j + direc[1]
            ret = ret or self.backtrack(mark,board,word,direction, n_i ,n_j,m,n,index+1)
        mark[i][j] = False 
        return ret
