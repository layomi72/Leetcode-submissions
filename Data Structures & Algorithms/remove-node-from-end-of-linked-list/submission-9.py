# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # total = length - n + 1
        length = 0
        current = head 
        
        while current:
            current = current.next
            length += 1


        total = length - n
        if total == 0:
            return head.next

        start = head
        i = 1
        while start:
            if total == i:
                start.next = start.next.next
                break
            else:
                start = start.next
                i += 1


        return head