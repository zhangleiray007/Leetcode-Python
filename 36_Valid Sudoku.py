class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            cur=[]
            for j in range(9):
                if  board[i][j] in cur:
                    return False
                else:
                    if board[i][j] != ".":
                        cur.append(board[i][j])  
                lenCur=len(cur)
                lenSet=len(set(cur))
                if lenCur != lenSet:
                    return False
                else:
                    pass
        for j in range(9):
            cur=[]
            for i in range(9):
                if  board[i][j] in cur:
                    return False
                else:
                    if board[i][j] != ".":
                        cur.append(board[i][j])  
                lenCur=len(cur)
                lenSet=len(set(cur))
                if lenCur != lenSet:
                    return False
                else:
                    pass
        
        for a in range(3):
            for b in range(3):
                cur=[]
                for i in range(3):
                    for j in range(3):
                        if  board[3*a+i][3*b+j] in cur:
                            return False
                        else:
                            if board[3*a+i][3*b+j] != ".":
                                cur.append(board[3*a+i][3*b+j])  
                        lenCur=len(cur)
                        lenSet=len(set(cur))
                        if lenCur != lenSet:
                            return False
                        else:
                            pass
        return True