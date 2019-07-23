class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1]*255
        start = 0 ;max_len=0
        for i in range(len(s)):
            if last[ord(s[i])] >= start:
                max_len = max(i-start, max_len)
                start = last[ord(s[i])] +1
            last[ord(s[i])] = i
            
        return max(len(s)-start, max_len)