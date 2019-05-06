#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.93%)
# Total Accepted:    117.3K
# Total Submissions: 317.2K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
class Solution:
    def findAnagrams(self, s, p):
        if s==None or len(s)<len(p):
            return []
        n=len(p)
        m=len(s)
        codep={}
        codes={}
        result = []
        for i in range(n):
            if p[i] in codep:
                codep[p[i]] +=1
            else:
                codep[p[i]]=1
        left, right = 0, 0
        while right < len(s):
            if s[right] in codep:
                codep[s[right]] -= 1
            while left <= right and (s[right] not in codep or codep[s[right]] < 0):
                if s[left] in codep:
                    codep[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1
        return result


a=Solution()
p= a.findAnagrams("cbaebabacd","abc")
print(p)
        

