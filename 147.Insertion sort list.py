# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-float('inf') - 1)
        dummy.next = head
        pre = dummy.next
        cur = pre.next
        while cur:
            if pre.val > cur.val:
                p = dummy
                while p.next.val <= cur.val:
                    p = p.next
                pre.next = cur.next
                cur.next = p.next
                p.next = cur
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return dummy.next