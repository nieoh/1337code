# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        
        start = ListNode(0)
        start.next = head
        node = start
        
        while node and node.next and node.next.next and node.next.next:
            node.next, node.next.next, node.next.next.next = node.next.next, node.next, node.next.next.next
            node = node.next.next
        return start.next
            
        
