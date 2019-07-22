class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0: return 0
        m = len(grid)
        n = len(grid[0])
        f = [[0 for i in range(n)] for j in range(m)]
        f[0][0] = grid[0][0]
        for i in range(1, n):
            f[0][i] = f[0][i-1] + grid[0][i]
        for i in range(1,m):
            f[i][0] = f[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = min(f[i-1][j],f[i][j-1])+grid[i][j]
        return f[m-1][n-1]