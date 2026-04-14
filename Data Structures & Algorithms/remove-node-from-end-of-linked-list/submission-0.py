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
        curr = head
        prev = None
        """
        1 -> 2 -> 3
        """
        while curr:
            """
            2
            3
            None
            """
            nextNode = curr.next
            """
            1 -> None
            2->1->None
            3 -> 2 -> 1 -> None
            """
            curr.next = prev
            """
            1
            2
            3
            """
            prev = curr
            """
            2
            3
            None
            """
            curr = nextNode
        revHead = curr = prev
        count=1
        """
        q: how do I track prev
        """
        prev = None
        while curr:
            if count==n:
                if prev != None:
                    prev.next=curr.next
                else:
                    revHead = revHead.next            
                break

            prev = curr
            curr = curr.next
            count+=1
        """
        Reverse again
        """
        prev = None
        curr = revHead
        """
        4 -> 2 -> 1
        """
        while curr:
            """
            2
            1
            None
            """
            nextNode = curr.next
            """
            4 -> None
            2 -> 4 -> None
            1 -> 2 -> 4 -> n
            """
            curr.next = prev
            """
            4
            2
            """
            prev = curr
            """
            2
            1
            """
            curr = nextNode

        return prev
            
      
        

            
        
        

