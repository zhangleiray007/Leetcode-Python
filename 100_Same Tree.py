# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if None in (p,q):
            return False
        else:
            return self.PreOrder(p,q)


    def PreOrder(self, pt,qt):
        if  pt and qt:
            return pt.val==qt.val and self.PreOrder(pt.left,qt.left) and self.PreOrder(pt.right, qt.right)
        else:
            return pt==qt