"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur =[root]
        while cur:
            next_r=[]
            for i in range(len(cur)):
                if i <len(cur)-1:
                    cur[i].next = cur[i+1]
               
                if cur[i].left: next_r.append(cur[i].left)
                if cur[i].right: next_r.append(cur[i].right)
            cur = next_r
        return root