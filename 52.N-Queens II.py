class Solution:
    
    def totalNQueens(self, n: int) -> int:
        
        def could_place(row,col):
            return not (cols[col] + hill_diag[row-col] + dale_diag[row+col])
        
        def place_queen(row,col):
            queens.add((row,col))
            cols[col] =1
            hill_diag[row-col]  = 1
            dale_diag[row+col] =1
            
        def remove_queen(row,col):
            queens.remove((row,col))
            cols[col] =0
            hill_diag[row-col]  = 0
            dale_diag[row+col] =0

        
        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row,col)
                    if row+1==n:
                        self.res = self.res+1
                    else:
                        backtrack(row+1)
                    remove_queen(row,col)
            
        
        cols = [0]*n
        hill_diag= [0]*(2*n-1)
        dale_diag= [0]*(2*n-1)
        self.res =0
        queens=set()
        backtrack()
        return self.res