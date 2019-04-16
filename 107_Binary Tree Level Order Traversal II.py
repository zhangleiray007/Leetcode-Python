class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Result=[]
        if not root:
            return Result
        curr=[root]
        while curr:
            level_r=[]
            next_r=[]
            for temp in curr:
                level_r.append(temp.val)
                if temp.left:
                    next_r.append(temp.left)
                if temp.right:
                    next_r.append(temp.right)
            Result.append(level_r)
            curr=next_r
        Result.reverse()
        return Result