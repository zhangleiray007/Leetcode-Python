class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 : return 0
        res = 0
        valley = prices[0]
        for i  in range(1,n):
            valley = min(valley, prices[i])
            res = max(res, prices[i]-valley)
        return res