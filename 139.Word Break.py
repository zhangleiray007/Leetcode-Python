class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False for i in range(n + 1)]
        f[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if f[j] and s[j: i] in wordDict:
                    f[i] = True
                    break
        return f[-1]