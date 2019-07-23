class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump=0
        n=len(nums)
        if n ==0: return False
        if n==1: return True
        for i in range(n):
            maxJump=maxJump-1
            if maxJump < nums[i]:
                maxJump = nums[i]
            if maxJump==0:
                return False
            if maxJump +i >=n-1:
                return True
        return False
		
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        n = len(nums)
        for i in range(n):
            if cover < i : return False
            cover = max(cover, nums[i] +i)
            if cover >= n-1 :
                return True
        return False