# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n==0 : return None
        if n==1: return lists[0]
        res = lists[0]
        for i in range(1,n):
            res = self.mergetwoLists(res,lists[i])
        return res
        
    def mergetwoLists(self, l1,l2):
        head = ListNode(0)
        dummy = head
        while l1 and l2:
            if l1.val > l2.val:
                head.next=l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1:
            head.next =l1
        if l2:
            head.next =l2
        return dummy.next
		
		
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n==0 : return None
        if n==1: return lists[0]
        nmod = n%2
        mmod =0
        m = n//2
        res = []
        for i in range(m):
            res.append(self.mergetwoLists(lists[2*i],lists[2*i+1]))
        if nmod ==1:
            res.append(lists[-1])
            m +=1
        while m >=2:
            res_tmp = []
            mmod = m%2
            m = m//2
            for i  in range(m):
                res_tmp.append(self.mergetwoLists(res[2*i],res[2*i+1]))
            if mmod ==1:
                res_tmp.append(res[-1])
                m +=1
            res = res_tmp.copy()
        if mmod ==1:
             res[0] = self.mergetwoLists(res[0],res[-1])
        return res[0]
        
    def mergetwoLists(self, l1,l2):
        head = ListNode(0)
        dummy = head
        while l1 and l2:
            if l1.val > l2.val:
                head.next=l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1:
            head.next =l1
        if l2:
            head.next =l2
        return dummy.next