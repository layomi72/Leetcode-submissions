# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head 
        current2 = head
        k = 0

        while (current2 != None):
            k += 1
            current2 = current2.next

        x = k - n 
        if (k - n == 0):
            return head.next
        
        for i in range(x -1):
            current = current.next 
        

        current.next = current.next.next

        return  head
