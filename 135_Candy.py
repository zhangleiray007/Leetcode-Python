class Solution:
    def candy(self, ratings: List[int]) -> int:
        n= len(ratings)
        if n==1 :
            return 1
        results=[1 for _ in range(n)]
        for i in range(1,n):
            if ratings[i-1] < ratings[i]:
                results[i]  =results[i-1] +1
        for i in range(1,n)[::-1]:
            if ratings[i-1] > ratings[i]:
                results[i-1] = max(results[i-1], results[i]+1)
        return sum(results)
