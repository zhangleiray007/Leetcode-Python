class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                if i == j:
                    j = nums[::-1].index(target - nums[i])
                    if i + j == len(nums) - 1 or j == IndexError:
                        continue
                    else:
                        return [i, len(nums) - 1-j]
                else:
                    return [i, j]
                    break
            else:
                continue
				
				
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            j = nums.index(target - nums[i]) if target - nums[i] in nums else None
            if i == j:
                j = nums[::-1].index(target - nums[i])
                if i + j == len(nums) - 1 or j == IndexError:
                    continue
                else:
                    return [i, len(nums) - 1-j]
            elif j==None:
                continue
            else:
                return [i, j]
                break
				
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            try:
                j =nums.index(target - nums[i])
            except ValueError as e:
                continue
            if i == j:
                j = nums[::-1].index(target - nums[i])
                if i + j == len(nums) - 1 or j == IndexError:
                    continue
                else:
                    return [i, len(nums) - 1-j]
            else:
                return [i, j]
                break
				
#best
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i