# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # split get to the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Reverse the second half of the list
        second = slow.next
        slow.next = None
        prev = None

        while second:
            nextt = second.next
            second.next = prev
            prev = second
            second = nextt
        
        start = head
        while start and prev:
            next2 = start.next
            start.next = prev 
            next3 = prev.next
            prev.next = next2
            start = next2
            prev = next3

        
