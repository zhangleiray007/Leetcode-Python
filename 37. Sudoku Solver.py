from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(9):
                        board[i][j] = str(1+k)
                        if (self.valid(board,i,j)  and self.solveSudoku(board) ):
                            return True
                        board[i][j] = '.'
                    return False
        return True
    def valid(self,board, x,y ):
        for i in range(9):
            if i!=x and board[x][y]==board[i][y]:
                return False
        for i in range(9):
            if i!=y and board[x][y]==board[x][i]:
                return False
        for i in range(3*(x//3),3*(x//3+1)):
             for j in range(3*(y//3),3*(y//3+1)):
                if (i!=x or j!=y)  and board[x][y]==board[i][j]:
                    return False
        return True

if __name__ == '__main__':
    grid = [["5","3",".",".","7",".",".",".","."],\
            ["6",".",".","1","9","5",".",".","."],\
            [".","9","8",".",".",".",".","6","."],\
            ["8",".",".",".","6",".",".",".","3"],\
            ["4",".",".","8",".","3",".",".","1"],\
            ["7",".",".",".","2",".",".",".","6"],\
            [".","6",".",".",".",".","2","8","."],\
            [".",".",".","4","1","9",".",".","5"],\
            [".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    solution.solveSudoku(grid)
    print(grid)

