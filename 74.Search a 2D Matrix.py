class Solution
    def searchMatrix(self, matrix List[List[int]], target int) - bool
        m = len(matrix)
        if m ==0 return False
        n = len(matrix[0])
        first = 0
        last = mn
        while first  last
            mid = first  + (last -first) 2
            value = matrix[midn][mid%n]
            if value == target
                return True
            elif value  target
                first = mid+1
            else 
                last = mid
            
        return False