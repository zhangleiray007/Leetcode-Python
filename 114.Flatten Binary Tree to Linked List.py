# Definition for a binary tree node.
# class TreeNode
#     def __init__(self, x)
#         self.val = x
#         self.left = None
#         self.right = None

class Solution
    def flatten(self, root TreeNode) - None
        
        Do not return anything, modify root in-place instead.
        
        if root 
            stack=[root]
        else
            stack=[]
        res = []
        while stack
            p = stack.pop()
            res.append(p.val)
            if p.right stack.append(p.right)
            if p.left stack.append(p.left)
        if root
            q=root
            for i in range(len(res)-1)
                q.val=res[i]
                q.left=None
                q.right=TreeNode(0)
                q = q.right
            q.val=res[-1] 
			

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        stack=[root]
        while stack:
            p = stack.pop()
            if p.right: stack.append(p.right)
            if p.left: stack.append(p.left)
            p.left=None
            if stack: p.right = stack[-1]