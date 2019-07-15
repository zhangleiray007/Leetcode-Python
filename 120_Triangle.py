class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows= len(triangle)
        for i in range(1,rows):
            for j in range(len(triangle[i])):
                if j==0:
                    triangle[i][j] = triangle[i-1][j] +  triangle[i][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j] = triangle[i-1][j-1] +  triangle[i][j]
                else:
                    triangle[i][j] = min( triangle[i-1][j-1],triangle[i-1][j] ) +  triangle[i][j]
        return min(triangle[-1])