# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        cur=pre.next
        nex=cur.next
        while nex:
            pre.next=nex
            cur.next=nex.next
            nex.next=cur
            pre=cur
            cur=cur.next
            nex = cur.next if cur!=None else None
        return dummy.next