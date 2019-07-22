class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m<n: return 0
        f = [[0 for i in range(n+1)] for j in range(m+1)]
        f[0][0]=1
        for i in range(1,m+1):
            f[i][0]=1
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    f[i][j]= f[i-1][j] + f[i-1][j-1]
                else:
                    f[i][j]=f[i-1][j]
        return f[m][n]