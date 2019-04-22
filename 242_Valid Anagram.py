class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sl=list(s)
        tl=list(t)
        sl.sort()
        tl.sort()
        if  sl==tl :
            return True
        else:
            return False