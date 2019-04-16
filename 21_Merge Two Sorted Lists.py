class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                tmp0 = cur.next
                tmp1 = l2.next
                cur.next = l2
                l2.next = tmp0
                l2 = tmp1
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next