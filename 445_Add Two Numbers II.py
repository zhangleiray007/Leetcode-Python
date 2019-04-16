# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = []
        nums2 = []
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        n1 = len(nums1)
        n2 = len(nums2)
        n = max(n1, n2)
        nums1.reverse()
        nums2.reverse()
        if n1 >= n2:
            nums2.extend([0] * (n1 - n2))
        else:
            nums1.extend([0] * (n2 - n1))


        l4 = [0 for _ in range(n)]

        for i in range(n):
            l4[i] = nums1[i] + nums2[i]
            if l4[i] >= 10:
                l4[i] = l4[i] - 10
                if i==n-1:
                    l4.append(1)
                    n=n+1
                else:
                    nums1[i + 1] = nums1[i + 1] + 1

        l3 = [ListNode(x) for x in l4[::-1]]
        for i in range(0, n - 1):
            l3[i].next = l3[i + 1]
        return l3[0]
                
                