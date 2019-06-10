#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s):
        slist=[]
        if s=="":
            return 0
        tmp=0
        length=0
        last=-1
        for i in range(0,len(s)):
            if s[i]=="(":
                slist.append(i)
            elif s[i] == ")":
                if len(slist) == 0:
                    last=i
                else:
                    slist.pop()
                    if len(slist) == 0:
                        if length < i-last:
                            length =i-last
                    else:
                        if length < i - slist[-1]:
                            length = i - slist[-1]
        return length

a=Solution()
w=a.longestValidParentheses("(()()")
print(w)
