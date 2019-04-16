# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur=new=tmp=ListNode(0)
        inh=0
        cur.next=new.next
        while l1!=None or l2!=None or inh!=0:
            if l1!=None and l2!=None:
                tmp = ListNode(0)
                tmp.val= (l1.val+l2.val+inh)%10
                inh=(l1.val+l2.val+inh)/10
                new.next=tmp
                new=new.next
                l1=l1.next
                l2=l2.next
            elif l1==None and l2!=None:
                tmp = ListNode(0)
                tmp.val= (l2.val+inh)%10
                inh=(l2.val+inh)/10
                new.next=tmp
                new=new.next
                l2=l2.next
            elif l2==None and l1!=None:
                tmp = ListNode(0)
                tmp.val= (l1.val+inh)%10
                inh=(l1.val+inh)/10
                new.next=tmp
                new=new.next
                l1=l1.next
            elif inh!=0:
                tmp = ListNode(0)
                tmp.val = (inh) % 10
                inh = (inh) / 10
                new.next = tmp
                new = new.next
        return cur.next