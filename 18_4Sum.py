class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        if len(nums)<4: return result
        nums.sort()
        for a in range(0,len(nums)-3):
            for b in range(a+1,len(nums)-2):
                c =b+1
                d=len(nums)-1
                while c<d:
                    if nums[a]+nums[b]+nums[c]+nums[d]<target:
                        c=c+1
                    elif nums[a]+nums[b]+nums[c]+nums[d]>target:
                        d=d-1
                    else:
                        result.append([nums[a],nums[b],nums[c],nums[d]])
                        c=c+1
                        d=d-1
        l2 = []

        for i in result:
            if not i in l2:
                l2.append(i)

        return l2