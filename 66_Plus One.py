class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        c=1
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=c
            c=digits[i]/10
            digits[i] %=10
        if c>0 :
            digits.insert(0,1)
        return  digits