#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.70%)
# Total Accepted:    340.1K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=s.lower()
        right=len(str)-1
        left=0
        while (left<right):
            if not ((str[left]>='a' and str[left]<='z') or (str[left]>='0' and str[left]<='9') ):
                left +=1
            elif not ((str[right]>='a' and str[right]<='z') or ((str[right]>='0' and str[right]<='9'))):
                right -=1
            elif str[left]!=str[right]:
                return False
            else:
                left +=1
                right -=1
        return True

