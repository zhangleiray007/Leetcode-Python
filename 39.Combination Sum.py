class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        candidates.sort()
        def backtrack(candidates, target, path, res):
            if target <0:
                return
            if target == 0:
                tmp = path.copy()
                tmp.sort()
                if  tmp not in res:
                    res.append(tmp)
                return

            for i in range(n):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(candidates, target - candidates[i], path, res)
                    path.pop()
                else:
                    return

        backtrack(candidates, target, path, res)
        return res
		

# 不排序的写法，只有遇到减到负数的时候剪枝

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        candidates.sort()
        def backtrack(candidates, target, path, res,start):
            if target <0:
                return
            if target == 0:
                res.append(path[:])
                return

            for i in range(start,n):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(candidates, target - candidates[i], path, res,i)
                    path.pop()
                else:
                    return

        backtrack(candidates, target, path, res,0)
        return res

https://leetcode-cn.com/problems/two-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
