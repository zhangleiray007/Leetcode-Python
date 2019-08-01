class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid):
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        marks = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not marks[i][j] and grid[i][j] == '1':
                    self.dfs(grid, i, j, m, n, marks)
                    count += 1
        return count

    def dfs(self, grid, i, j, m, n, marks):
        marks[i][j] = True
        for direction in self.directions:
            n_i = i + direction[0];
            n_j = j + direction[1]
            if 0 <= n_i < m and 0 <= n_j < n and not marks[n_i][n_j] and grid[n_i][n_j] == '1':
                self.dfs(grid, n_i, n_j, m, n, marks)