class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reversel(s,start,end):
            if start>=end:
                return 
            s[start],s[end] = s[end],s[start]
            return reversel(s,start+1,end-1)
        
        reversel(s,0,len(s)-1)