class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        N= len(s1)
        if N != len(s2):
            return False
        f = [[[False for i in range(N)] for j in range(N)] for k in range(N+1)]
        for i in range(N):
            for j in range(N):
                f[1][i][j] =(s1[i]==s2[j])
        for n in range(1,N+1):
            for i in range(N-n+1):
                for j in range(N-n+1):
                    for k in range(1,n):
                        if (f[k][i][j] and f[n-k][i+k][j+k]) \
                        or (f[k][i][j+n-k] and f[n-k][i+k][j] ):
                            f[n][i][j]=True
                            break;
                            
        return f[N][0][0]