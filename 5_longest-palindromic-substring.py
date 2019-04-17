#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.99%)
# Total Accepted:    524.2K
# Total Submissions: 1.9M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        maxlen = 1
        sstart = 0
        n = len(s)

        for i in range(n):
            begin = i - 1
            end = i + 1
            while begin >= 0 and end < n and s[begin] == s[end]:
                if end - begin + 1 >= maxlen:
                    maxlen = end - begin + 1
                    sstart = begin
                begin -= 1
                end += 1

        for i in range(n):
            begin = i
            end = i + 1
            while begin >= 0 and end < n and s[begin] == s[end]:
                if end - begin + 1 >= maxlen:
                    maxlen = end - begin + 1
                    sstart = begin
                begin -= 1
                end += 1
        if maxlen != -1:
            return s[sstart:sstart + maxlen]
        return ""

