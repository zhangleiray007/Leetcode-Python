# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.balanceHeight(root)>=0
    def balanceHeight(self, root):
        if not root : return 0
        left = self.balanceHeight(root.left)
        right = self.balanceHeight(root.right)
        if left<0 or right<0 or abs(left-right)>1: 
            return -1
        return max(left, right)+1