# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None or k < 2:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        end = head
        while end:
            for i in range(1, k):
				end = None if end==None or end.next==None else end.next
            if end == None:
                break
            pre = self.reverse(pre, pre.next, end)
            end = pre.next
        return dummy.next

    def reverse(self, pre, begin, end):
        end_next = end.next
        cur = begin
        post = cur.next
        while post != end_next:
            cur.next = post.next
            post.next = pre.next
            pre.next = post
            post = cur.next
        cur.next=end_next
        return cur