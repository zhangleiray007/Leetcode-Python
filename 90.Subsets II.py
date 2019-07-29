class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n == 0 : return res
        nums.sort()
        selected = [False] * n
        self.subset(nums, selected, 0, res)
        return res
    
    def subset(self, nums, selected, step, res):
        if step == len(nums):
            sub = []
            for i in range(len(nums)):
                if selected[i] :
                    sub.append(nums[i])
            if sub not in res:
                res.append(sub)
            return
        selected[step]=False
        self.subset(nums,selected,step+1,res)
        selected[step]=True
        self.subset(nums,selected,step+1,res)