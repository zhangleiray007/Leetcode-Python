class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        cur = [root]
        while cur:
            level_r=[]
            next_r=[]
            for temp in cur:
                level_r.append(temp.val)
                if temp.left: next_r.append(temp.left)
                if temp.right: next_r.append(temp.right)
            res.append(level_r)
            cur = next_r
        return res