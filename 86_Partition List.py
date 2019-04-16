# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_dummy=ListNode(-1)
        right_dummy=ListNode(-1)
        
        left_cur=left_dummy
        right_cur=right_dummy
        while head: 
            cur=head
            if cur.val < x:
                left_cur.next=cur
                left_cur=cur
            else:
                right_cur.next=cur
                right_cur=cur
            head =head.next
        left_cur.next=right_dummy.next
        right_cur.next=None
        
        return left_dummy.next