class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        first=0
        last=len(nums)
        while first!=last:
            mid=first +(last-first)/2
            if nums[mid]==target:
                return True
            if nums[first]<nums[mid]:
                if nums[first]<=target and target < nums[mid]:
                    last=mid
                else:
                    first=mid+1
            elif nums[first]>nums[mid]:
                if nums[mid]<target and target<=nums[last-1]:
                    first=mid+1
                else:
                    last=mid
            else:
                first=first+1
        return False