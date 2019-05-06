#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack_dirs=[]
        N=len(path)
        i=0
        while i<N and i !=-1:
            i +=1
            j=path.find('/',i,len(path))
            if j!=-1:
                dirs=path[i:j]
            else:
                dirs = path[i:]
            if dirs!='' and dirs !="." :
                if dirs=="..":
                    if stack_dirs!=[]:
                        stack_dirs.pop()
                else:
                    stack_dirs.append(dirs)
            i=j
        result=""
        if stack_dirs==[]:
            return "/"
        else:
            for d in stack_dirs:
                result=result+"/"
                result=result+str(d)
            return result