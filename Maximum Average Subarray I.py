class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        maxsum=cursum=sum(nums[0:k])
        for i in range(n-k+1):
            cursum= max(cursum, sum(nums[i:i+k]))
            maxsum = max(maxsum, cursum)
        return maxsum/k



a =Solution()
w = a.findMaxAverage([1,12,-5,-6,50,3],4)
print(w)