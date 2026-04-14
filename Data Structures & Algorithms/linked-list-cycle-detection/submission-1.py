# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
q: How do we determine if a node has already been visited?
A: Not sure, can't do it solely based off value because there can 
be duplicate values. 
 
Maybe you store all visted nodes in an array? 
Check if current node has already been visited or not
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        curr=head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr=curr.next
        return False