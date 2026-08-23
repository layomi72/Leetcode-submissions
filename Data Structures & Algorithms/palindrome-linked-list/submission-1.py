# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head 

        current = head
     

        # if fast = none then even if fast.next = none then its odd
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow
        prev = None

        while second:
            nextt = second.next
            second.next = prev
            prev = second
            second = nextt
     

        while current and prev:
            if current.val != prev.val:
                return False

            else:
                current = current.next
                prev = prev.next

        return True