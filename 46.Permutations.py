class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(first = 0):
            if first == n:
                res.append(nums[:])
                return
            for i in range(first,n):
                nums[first],nums[i] =  nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i] =  nums[i],nums[first]
        
        backtrack()
        return res