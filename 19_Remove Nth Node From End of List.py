# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy= ListNode(-1)
        dummy.next=head
        p =dummy
        q =dummy
        for i in range(n):
            q=q.next
        while q.next:
            p=p.next
            q=q.next
        p.next=p.next.next
        return dummy.next