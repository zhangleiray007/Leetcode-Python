class Solution(object):
    def isValid(self, s):
        slist=[""]
        if s=="":
            return True
        for i in range(0,len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                slist.append(s[i])
            elif s[i]==")" or s[i]=="}" or s[i]=="]":
                if s[i]==")"  and slist[-1] =="(" :
                    slist.pop()
                elif   s[i]=="}"  and slist[-1] =="{" :
                    slist.pop()
                elif   s[i]=="]"  and slist[-1] =="[" :
                    slist.pop()
                else:
                    return False
            else:
                return False
        if len(slist) == 1:
            return True
        else:
            return False
			
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []