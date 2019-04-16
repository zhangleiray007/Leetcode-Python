class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack=[]
        result=ListNode(-1)
        reHead=
		
        while head:
            stack.append(head.val)
            head=head.next
        n=len(stack)
        for i in range(n):
            node=ListNode(stack.pop())
            result.next=node
            result=result.next
        return reHead.next
		
		
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev

		
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if head == None or head.next == None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy.next
        head = head.next
        while head:            
            prev.next=head.next            
            head.next=dummy.next
            dummy.next=head  
            head=prev.next
        return dummy.next
		

class Solution:
    def reverseList(self, head):
        return reverse(head)

    def reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return reverse(n, node)
