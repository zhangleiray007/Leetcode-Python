class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res =[]
        path = []
        candidates.sort()
        def backtrack(candidates, path,res, target, start):
            if target < 0: return
            if start> n: return 
            if target ==0:
                if path[:] not in res:
                    res.append(path[:])
                return
            for i in range(start,n):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(candidates,path,res,target - candidates[i], i+1)
                    path.pop()
                else:
                    return 
        
        backtrack(candidates,path,res,target,0)
        return res