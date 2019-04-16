class Solution(object):
    def romanToInt(self, s):
        value=0
        m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = m[s[0]]
        for i in range(1,len(s)):
            if m[s[i-1]] < m[s[i]]:
                value =value +m[s[i]]-2*m[s[i-1]]
            else:
                value =value + m[s[i]]
        return value