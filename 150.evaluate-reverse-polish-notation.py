#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
class Solution:
    def evalRPN(self, tokens):
        stack = []
        n = len(tokens)
        if n ==0: return 0
        res = 0
        for i in range(n):
            if tokens[i] != '+' and  tokens[i] != '-' and tokens[i] != '*'\
               and tokens[i] != '/':
                stack.append(int(tokens[i]))
                res = int(tokens[i])
            elif tokens[i] == '+':
                tmp0 = stack.pop()
                tmp1 = stack.pop()
                res = tmp0+tmp1;
                stack.append(res)
            elif tokens[i] == '-':
                tmp0 = stack.pop()
                tmp1 = stack.pop()
                res = tmp1-tmp0;
                stack.append(res)
            elif tokens[i] == '*':
                tmp0 = stack.pop()
                tmp1 = stack.pop()
                res = tmp0*tmp1;
                stack.append(res)
            elif tokens[i] == '/':
                tmp0 = stack.pop()
                tmp1 = stack.pop()
                if tmp0 <0 and tmp1<0:
                    res = abs(-tmp1 // -tmp0);
                elif  tmp0 <0:
                    res = -abs(tmp1 // -tmp0);
                elif  tmp1 <0:
                    res = -abs(-tmp1 // tmp0);
                else:
                    res = tmp1 // tmp0;
                stack.append(res)
        return res

a = Solution()
w = a.evalRPN(["4","-2","/","2","-3","-","-"])
print(w)