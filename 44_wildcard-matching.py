#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pP=sP=ss=0; star=-1
        while sP < len(s):
            if pP<len(p) and (s[sP] == p[pP] or p[pP]=='?'):
                sP +=1; pP +=1
                continue
            if pP<len(p) and p[pP]=='*':
                star = pP; pP +=1; ss=sP
                continue
            if  star !=-1:
                pP =star+1;ss +=1; sP=ss
                continue
            return False
        while pP<len(p) and p[pP] =='*':
            pP +=1
        if  pP==len(p): return True
        return False

a=Solution()
w=a.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
)
print(w)


