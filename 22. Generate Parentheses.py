class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        path =[]
        if n>0:
            self.generate(n,path,res, 0,0)
        return res
    def generate(self,n,path,res, l,r):
        if l == n:
            path.append(')'*(n-r))
            res.append(''.join(path[:]))
            path.pop()
            return
        path.append('(')
        self.generate(n,path,res,l+1,r)
        path.pop()
        if (l>r):
            path.append(')')
            self.generate(n,path,res,l,r+1)
            path.pop()