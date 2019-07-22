class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        f = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            f[i][0] = i
        for j in range(n+1):
            f[0][j] = j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    f[i][j]=f[i-1][j-1]
                else:
                    mn = min(f[i-1][j],f[i][j-1])
                    f[i][j] = 1+ min(f[i-1][j-1],mn)
        return f[m][n]