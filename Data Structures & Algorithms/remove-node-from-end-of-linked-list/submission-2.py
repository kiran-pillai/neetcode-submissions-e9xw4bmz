# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
q: how do we find the nth node from the back?
a: reverse linked list, remove nth node, reverse back

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        dummy = ListNode(0, head)
        l = dummy
        curr = head
        count = 1
        r = head
        while n>0:
            r = r.next
            n-=1
        
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next

            
      
            
      
        

            
        
        

