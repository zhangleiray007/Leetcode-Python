class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlist=[]
        if len(nums)<3:
            return rlist
        target=0
        last=len(nums)
        nums.sort()
        for i in range(0,len(nums)-2):
            j=i+1
            if i>0 and nums[i]==nums[i-1]:
                continue
            k=last-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<target:
                    j=j+1
                    while nums[j]==nums[j-1] and j<k:
                        j=j+1
                elif nums[i]+nums[j]+nums[k]>target:
                    k=k-1
                    while nums[k]==nums[k+1] and j<k:
                        k=k-1
                else:
                    rlist.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    while nums[j]==nums[j-1] and nums[k]==nums[k+1] and j<k:
                        j=j+1
        return rlist