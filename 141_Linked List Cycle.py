# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        dicts={}
        while head:
            if head not in dicts.keys():
                dicts[head]=1
                head=head.next
            else:
                return True
        return False
            