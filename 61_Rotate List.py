# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head== None or k==0:
            return head
        len=1
        p=head
        while(p.next):
            len +=1
            p=p.next
        p.next=head
        k=len-k%len
        for i in range(k):
            p=p.next
        head=p.next
        p.next=None
        return head