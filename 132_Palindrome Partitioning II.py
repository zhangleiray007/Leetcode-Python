class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        f =[n-1-i for i in range(n+1)]
        for i  in reversed(range(n)):
            for j in range(i,n):
                if s[i]==s[j] and ((j-i<=1) or dp[i+1][j-1]) :
                    dp[i][j]=1
                    f[i] = min(f[i], f[j+1]+1)
        return f[0]