class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr=head
        reversedLinkedList=None
        while curr:
            newNode=ListNode(curr.val)
            newNode.next=reversedLinkedList
            reversedLinkedList=newNode
            curr=curr.next
        return reversedLinkedList