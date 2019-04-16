# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        cur=dummy
        a=0.1 
        while head:
            if a ==head.val:
                    cur=pre
                    cur.next=head.next
                    head=head.next                
            else:
                a=head.val
                head = head.next                
                pre = cur
                cur = cur.next
                
        return dummy.next

		
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
            
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        cur=dummy.next
        
        while cur!=None:
            while cur.next and cur.next.val==pre.next.val:
                cur=cur.next
            if pre.next==cur:
                pre=pre.next
            else:
                pre.next=cur.next
            cur=cur.next
        return dummy.next
