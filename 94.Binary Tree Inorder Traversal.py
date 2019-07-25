# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        p = root
        while stack or p:
            if p:
                stack.append(p)
                p=p.left
            else:
                p =stack.pop()
                res.append(p.val)
                p=p.right
        return res