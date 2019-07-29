# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
		
# class Solution:
    # def preorderTraversal(self, root):
        # res = []
        # stack = [root]
        # while stack:
            # node = stack.pop()
            # if node:
                # res.append(node.val)
                # stack.append(node.right)
                # stack.append(node.left)
        # return res
		
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        if root:  stack=[root]
        while stack:
            p= stack.pop()
            res.append(p.val)
            if p.right: stack.append(p.right)
            if p.left:  stack.append(p.left)
        return res

