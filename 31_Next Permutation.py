class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        partition = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                partition = i - 1
                break
        if partition == -1:
            nums.reverse()
            # return nums
        else:
            for j in range(len(nums)-1, partition, -1):
                if nums[partition] < nums[j]:
                    nums[partition], nums[j] = nums[j], nums[partition]
                    break
            left = partition + 1
            nums[left:] = sorted(nums[left:])
