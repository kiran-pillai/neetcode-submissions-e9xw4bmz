# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. Determine start of p2
2. Reverse p2
3. Merge p1 and p2 
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
                return 
        
        slow, fast = head, head
        # Guarantees we will get slow pointer to half way of list by end
        while fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
        p2 = slow.next
        # Break connection for p1 list
        slow.next = None
        # Initialize tail
        prev = None
        # 3->4->5 -> None
        # 3->null
        # 4->3->null
        # STOPPED HERE, I'M MESSING UP THE REVERSAL OF LINKED LIST
        while p2:
                nextNode=p2.next
                # 3 -> null
                # 4 -> 3
                p2.next=prev
                #  prev = 3
                #  prev =4
                prev=p2
                #  4
                #  5
                p2=nextNode
        p2 = prev
        p1 = head
        """
        p1 = 1->2->3
        p2 = 5 -> 4
        """
        while p2:
                p1Next=p1.next
                p2Next=p2.next
                p1.next = p2
                p2.next=p1Next
                p2=p2Next
                p1=p1Next


                



        
        
        
        



            
            

            