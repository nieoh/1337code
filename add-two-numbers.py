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
        
        
        carry = 0
        head = ListNode(0)
        snode = head
        
        while l1 and l2:
            ssum = l1.val + l2.val + carry
            if ssum >= 10:
                carry = 1
                snode.next = ListNode(ssum%10)
            else:
                carry = 0
                snode.next = ListNode(ssum)
            snode = snode.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            ssum = l1.val + carry
            if ssum >= 10:
                carry = 1
                snode.next = ListNode(ssum%10)
            else:
                carry = 0
                snode.next = ListNode(ssum)
            snode = snode.next
            l1 = l1.next
            
        while l2:
            ssum = l2.val + carry
            if ssum >= 10:
                carry = 1
                snode.next = ListNode(ssum%10)
            else:
                carry = 0
                snode.next = ListNode(ssum)
            snode = snode.next
            l2 = l2.next
                
        if carry > 0:
            snode.next = ListNode(carry)
        return head.next
