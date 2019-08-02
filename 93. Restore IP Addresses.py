class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        self.dfs(s, path, res, 0)
        return res

    def dfs(self, s, path, res, start):
        if len(path) == 4 and start == len(s):
            res.append(path[0] + '.' + path[1] + '.' + path[2] + '.' + path[3])
            return
        if len(s) - start > (4 - len(path)) * 3:
            return
        if len(s) - start < 4 - len(path):
            return
        num = 0
        for i in range(start, start + 3):
            if i >=len(s):
                continue
            num = num * 10 + ord(s[i]) - ord('0')
            if num < 0 or num > 255:
                continue
            path.append(s[start:i + 1])
            self.dfs(s, path, res, i + 1)
            path.pop()
            
            if num==0: break