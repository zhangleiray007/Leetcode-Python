class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        if n <2: return 0
        f = [0]*n
        g = [0]*n
        valley = prices[0]
        for i in range(1,n):
            valley = min(valley, prices[i])
            f[i] = max(f[i-1], prices[i] - valley)
        peak = prices[n-1]
        for i in range(n-2, -1, -1):
            peak = max(peak, prices[i])
            g[i] = max(g[i+1], peak - prices[i])
        for i in range(n):
            res = max(res, f[i]+g[i])
            
        return res