class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        else:
            n=nums.count(val)
            for i in range(0,n):
                nums.remove(val)
            return len(nums)