class Solution(object):
    def saysay(self, s):
        rstr = ""
        tmp = s[0]
        n = 1
        for i in range(0,len(s)-1):
            if (s[i]==s[i+1]):
               n=n+1
            else:
                rstr=rstr+`n`+tmp
                n=1
                tmp=s[i+1]
        return rstr+`n`+tmp
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        n=n-1
        while (n):
            s = self.saysay(s)
            n=n-1
        return s