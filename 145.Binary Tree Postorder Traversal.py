# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # stack =[]
        # p=root
        # pre_p=None
        # flag = 1
        # while flag:
            # while p:
                # stack.append(p)
                # p=p.left
            # pre_p=None
            # while stack:
                # p=stack.pop()
                # if p.right ==pre_p:#right child is None or has been accessed
                    # res.append(p.val)
                    # pre_p = p
                # else:
                    # stack.append(p)
                    # p = p.right
                    # break
            # if not stack: flag=0
        # return res
		
		
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return None
        res = []
        stack =[root]
        head = root
        while stack:
            t = stack[-1]
            if ((not t.left) and (not t.right))  or t.left == head or t.right == head:
                res.append(t.val)
                stack.pop()
                head =t
            else:
                if t.right: stack.append(t.right)
                if t.left:  stack.append(t.left)
        return res
            
            