#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
class Solution:
    def largestRectangleArea(self, heights):
        n=len(heights)
        maxArea = 0
        L_left = [0] * n
        L_right =  [0] * n
        if n == 0:
            return heights[0]
        # Extend right
        L_right[n-1] = 1
        for i in range(n-2, -1 ,-1):
            if (heights[i] > heights[i+1]):
                L_right[i] = 1
            else:
                j = i+1
                while j< n  and  heights[j] >= heights[i]:
                    j += L_right[j]
                L_right[i] = j - i

        L_left[0] =1
        for i in range(1,n):
            if heights[i] > heights[i-1]:
                L_left[i] = 1
            else:
                j = i-1
                while j>=0 and heights[j] >= heights[i]:
                    j -= L_left[j]
                L_left[i]= i-j

        maxArea = heights[0]
        for i in range(n):
            maxArea = max(heights[i] *(L_left[i] + L_right[i]-1) ,maxArea)

        return maxArea


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n=len(heights)
        maxArea = 0
        stack = []

        for i in range(n):
            if not stack or  heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                while stack and  heights[i] <= heights[stack[-1]]:
                    h= heights[stack[-1]]
                    stack.pop()
                    w= i if not stack else i-stack[-1]-1
                    maxArea = max(maxArea, h * w)
                stack.append(i)
        return maxArea