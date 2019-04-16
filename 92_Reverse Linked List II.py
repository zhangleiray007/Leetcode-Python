# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head:
            k=1
        else:
            return None
        prev=None
        headtmp=head
        while head:
            if k==m-1:
                headpre=head
                cur=head
                head=head.next
                k +=1
            elif k==m:
                cur=head
                prev=head
                head=head.next
                tailpre=prev
                k +=1
            elif k>m and k<n :
                cur=head
                head=head.next
                cur.next=prev
                prev=cur
                k += 1
            elif k==n:
                cur=head
                head=head.next
                cur.next=prev
                prev=cur
                tailpre.next=head
                if m!=1:
                    headpre.next=prev
                    return headtmp
                else:
                    return prev
            else:
                head=head.next
                k +=1
        return headtmp
		
		
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        prev = dummy
        for i in range(m - 1):
            prev = prev.next
        head2 = prev

        prev= head2.next
        cur = prev.next
        for i in range(n - m):
            prev.next=cur.next
            cur.next= head2.next //
            head2.next=cur       //在head2和pre中插入cur
            cur=prev.next
        return dummy.next
        return headtmp