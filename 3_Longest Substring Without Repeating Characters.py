class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=""
        nums=0
        tmps=0
        for i in range(0,len(s)):
            if s[i] in lst:
                mm=lst.index(s[i])
                if mm==len(lst)-1:
                    lst=""
                    lst=lst+s[i]
                    if tmps > nums:
                        nums = tmps
                    tmps=1
                else:
                    lst=lst[mm+1::]
                    lst = lst + s[i]
                    if tmps > nums:
                        nums = tmps
                    tmps=tmps-mm


            else:
                lst=lst+s[i]
                tmps=tmps+1
        if tmps > nums:
            nums = tmps
        return nums