#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1); n = len(s2)
        if m +n  != len(s3):
            return False
        f = [[True for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            f[i][0]= f[i-1][0] and s1[i-1]== s3[i-1]
            
        for i in range(1,n+1):
            f[0][i] = f[0][i-1] and s2[i-1]== s3[i-1]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                f[i][j] = ((s1[i-1] == s3[i+j-1]) and f[i-1][j]) or ((s2[j-1] == s3[i+j-1]) and f[i][j-1])
        return f[m][n]
s1="a"
s2=""
s3="c"

a = Solution()
w= a.isInterleave(s1,s2,s3)
print(w)
