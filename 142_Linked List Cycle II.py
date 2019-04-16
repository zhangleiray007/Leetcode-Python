# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return None
        dicts={}
        while head:
            if head not in dicts.keys():
                dicts[head]=1
                head=head.next
            else:
                return head
        return None
		
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return None
        slow = fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                tmp=head
                while tmp !=fast:
                    tmp=tmp.next
                    fast= fast.next
                return tmp
        return None