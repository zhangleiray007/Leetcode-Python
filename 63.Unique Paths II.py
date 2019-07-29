class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]: return 0
        f = [[0 for i in range(n)] for j in range(m)]
        f[0][0]=1
        for i in range(1,m):
            f[i][0]= f[i-1][0] if obstacleGrid[i][0] ==0    else 0
        for i in range(1,n):
            f[0][i]=f[0][i-1]  if obstacleGrid[0][i] ==0  else 0
        for i in range(1,m):
            for j in  range (1,n):
                f[i][j] = f[i-1][j] +f[i][j-1]  if obstacleGrid[i][j] ==0  else 0
        return f[m-1][n-1]
		
		
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m-1][n-1]: return 0
        self.f = [[0 for i in range(n)] for j in range(m)]
        self.f[0][0]=1
        return self.dfs(obstacleGrid,m-1,n-1)
    
    def dfs(self, obstacleGrid, x,y):
        if x<0 or y <0: return 0
        if obstacleGrid[x][y]: return 0
        if x==0 and y ==0: return self.f[0][0]
        
        if self.f[x][y]>0:
            return self.f[x][y]
        else:
            self.f[x][y] =self.dfs(obstacleGrid,x-1,y) + self.dfs(obstacleGrid,x,y-1)
            return self.f[x][y]