# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return None
        dummy=ListNode(-1)
        dummy.next=head
        
        slow=fast=head
        pre = None
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
            
        pre.next=None
        slow = self.reverse(slow)
        
        cur=head
        while cur.next:
            tmp=cur.next
            cur.next=slow
            slow=slow.next
            cur.next.next=tmp
            cur =tmp
        cur.next=slow
        
    def reverse(self, head):
        if head == None or head.next==None:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        cur=head
        post=head.next
        while post:
            cur.next=post.next
            post.next=pre.next
            pre.next=post
            post=cur.next
        return dummy.next