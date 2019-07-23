class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start = 0; end = n-1 ; max_res = 0
        while (start < end ):
            max_res = max(max_res, min(height[start], height[end])* (end-start))
            if height[start]< height[end]:
                start = start +1
            else:
                end = end -1
        return max_res