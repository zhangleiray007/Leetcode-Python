# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        else:
            return self.PreOrder(root, root)

    def PreOrder(self, pt, qt):
        if pt == None and qt == None:
            return True
        if pt == None or qt == None:
            return False

        return pt.val == qt.val and self.PreOrder(pt.left, qt.right) and self.PreOrder(pt.right, qt.left)