#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
class Solution:
    def maximalRectangle(self, matrix):
        res =0 
        m = len(matrix)
        if m ==0 :
            return 0
        n = len(matrix[0])
        height = [0]* n
        for i in range(m):
            for j in range(n):
                height[j] = 0 if matrix[i][j] =='0' else height[j]+1
            res = max(res, self.largestRectangleArea(height))
        return res
        
    
    def largestRectangleArea(self, heights):
        heights.append(0)
        stack = []
        maxArea =0 
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]]>= heights[i]:
                h = heights[stack[-1]]
                stack.pop()
                w= i if not stack else i-stack[-1]-1
                maxArea = max(maxArea, h*w)
            stack.append(i)
        return maxArea




class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res =0 
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        left = [0] *  n
        right = [n] * n
        height =[0] * n
        
        for i  in range(m):
            cur_left=0;cur_right=n
            for j in range(n):
                height[j] = 0 if matrix[i][j] =='0' else height[j]+1
            
            for j in range(n):
                if matrix[i][j] =='1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j]=0
                    cur_left = j +1
            
            for j in reversed(range(n)):
                if matrix[i][j] =='1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] =n
                    cur_right = j
            
            for j in range(n):
                res = max(res, (right[j]-left[j]) * height[j])
                
            
        return res