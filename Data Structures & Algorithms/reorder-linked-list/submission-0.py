# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_pointer = head
        fast_pointer = head.next
        current = head
        temp2 = None
        prev = None 
        temp1 = None
        while(fast_pointer != None and fast_pointer.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        second_half = slow_pointer.next
        slow_pointer.next = None

        while(second_half != None):
            temp1 = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp1

        current2 = prev
        while (current != None and current2 != None):
            temp1 = current.next
            temp2 = current2.next
            current.next = current2
            current2.next = temp1
            current = temp1
            current2 = temp2

        return None


        