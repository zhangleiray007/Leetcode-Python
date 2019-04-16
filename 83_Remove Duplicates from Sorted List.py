class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
			return head
        vl = head.val
        dummy = ListNode(0)
        dummy.next = head
        while  head.next !=None:
            cur = head.next
            if vl == cur.val:
                head.next = cur.next
                vl = head.val
            else:
                head = head.next
                vl = head.val
        return dummy.next