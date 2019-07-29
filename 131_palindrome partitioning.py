class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[-1] = [[]]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    for each in dp[j]:
                        dp[i].append([s[i:j]] + each)
        return dp[0]
		
		
class Solution:
    def partition(self, s):
        res = []
        path =[]
        self.dfs(s, path,res,0,1)
        return res
    
    def dfs(self, s,path,res,pre,start):
        if start == len(s):
            if s[pre:start] == s[pre:start][::-1]:
                path.append(s[pre: start])
                res.append(path.copy())
                path.pop()
            return
        self.dfs(s,path,res,pre,start+1)
        if s[pre: start] == s[pre: start][::-1]:
            path.append(s[pre: start])
            self.dfs(s,path,res,start,start+1)
            path.pop()
            
			
class Solution:
    def partition(self, s):
        if not s:
            return [[]]
        self.res =[]
        self.dfs(s,[])
        return self.res
    
    def dfs(self,s,path):
        if len(s)==0:
            self.res.append(path)
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                self.dfs(s[i+1:],path+[s[:i+1]])