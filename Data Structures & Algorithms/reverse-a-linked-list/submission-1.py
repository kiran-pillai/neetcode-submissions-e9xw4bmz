class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = new_ll = None
        curr = head
        while curr:
            init_node = ListNode(curr.val)
            init_node.next = new_ll
            new_ll = init_node
            curr = curr.next
        return new_ll
        