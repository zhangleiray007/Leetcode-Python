class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        m=s.split()

        if len(m)==0:
            return 0
        else:
            return len(m[-1])