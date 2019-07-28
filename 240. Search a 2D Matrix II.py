class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m ==0: 
            return False
        n = len(matrix[0])
        i = m -1
        j = 0
        while i >=0 and j < n:
            if matrix[i][j] == target:
                return  True
            elif matrix[i][j] > target:
                i -=1            
            else:
                j +=1
                
        return  False