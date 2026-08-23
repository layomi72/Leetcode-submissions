# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
    

        dummy = ListNode(0)
        head1 = dummy
        dummy.next = current

        while dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        if dummy.val == val:
            prev.next = prev.next.next

        return head1.next