import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rlist=[]
        if len(nums)<3:
            return rlist
        result=0
        nums.sort()
        min_gap=sys.maxsize

        for i in range(0,len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                sumd=nums[i]+nums[j]+nums[k]
                gap=abs(sumd-target)
                if gap<min_gap:
                    result=sumd
                    min_gap=gap
                if sumd<target:
                    j=j+1
                else:
                    k=k-1
        return result