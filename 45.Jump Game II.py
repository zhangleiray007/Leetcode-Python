class Solution:
    def jump(self, nums: List[int]) -> int:
        level = 0; last_cover=0; cur_cover=0
        n= len(nums)
        for i in range(n):
            if (last_cover < i):
                last_cover = cur_cover
                level +=1
            elif (last_cover >= n -1):
                return level
            cur_cover = max(cur_cover, nums[i]+i)
        return level